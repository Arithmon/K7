"""Generate manifest, paper tables, limitations, macros and figures from JSON."""
from fractions import Fraction
from io import BytesIO
import json
import re
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from common import ROOT, read, sha, metric_hash, validate_freeze, validate_metric_input, validate_result

RESULTS = ["nk_certificate","hodge2_matching","hodge3_matching","adiabatic_bound",
           "scalar_spectrum","weyl_law","kk_tower","hodge_profiles","intersection_form",
           "democracy_check","lambda1_enclosure","lambda1_check"]

def entry(identifier, source, key, status, kind, section, theorem, scope, required=False):
    data=read("results/"+source+".json")
    return {"id":identifier,"value":data.get("values",{}).get(key) if key else None,
            "claim_status":status,"evidence_kind":kind,"section":section,
            "theorem":"THEOREMS.md#"+theorem,"scope":scope,"submission_required":required,
            "script":"scripts/"+{"nk_certificate":"metric_certificate","hodge_profiles":"hodge_profiles"}.get(source,source)+".py",
            "result_json":"results/"+source+".json","value_path":"values."+key if key else None,
            "result_sha256":sha(ROOT/"results"/(source+".json")),
            "metric_sha256":data["metric_sha256"],"source_commit":data["source_commit"],
            "input_hashes":data["provenance"],
            "blocked_by":data.get("blocked_by",[]) if status in ["PENDING","CONDITIONAL"] else []}

def build_manifest():
    validate_freeze()
    validate_metric_input()
    for name in RESULTS:validate_result("results/"+name+".json")
    claims=[]
    for key in ["zero","one","two","dimension","left_endpoint","right_endpoint","parameter_count","determinant"]:
        claims.append(entry(key,"nk_certificate",key,"CERTIFIED","exact","Geometry","t-metric-reconstruction-positivity-and-determinant",
                            "Model definition or exact algebraic property of the frozen coordinate ansatz"))
    def add(*args,**kwargs):claims.append(entry(*args,**kwargs))
    add("nk","nk_certificate",None,"PENDING","pending","Metric certificate","t-nk-contract-what-a-valid-replacement-must-specify",
        "Torsion-free existence relative to a specified K3 input",True)
    add("product_h_two","hodge2_matching","product_h_two","CERTIFIED","exact","Matching",
        "t-product-cohomology-diagnostic-not-a-matching-lemma","Kunneth arithmetic for ordinary cohomology of the bare product")
    add("product_h_three","hodge3_matching","product_h_three","CERTIFIED","exact","Matching",
        "t-product-cohomology-diagnostic-not-a-matching-lemma","Kunneth arithmetic for ordinary cohomology of the bare product")
    add("matching_two","hodge2_matching",None,"PENDING","pending","Matching",
        "t-product-cohomology-diagnostic-not-a-matching-lemma","Kernel of the required end-matching complex",True)
    add("matching_three","hodge3_matching",None,"PENDING","pending","Matching",
        "t-product-cohomology-diagnostic-not-a-matching-lemma","Degree-three matching kernel and completeness",True)
    add("adiabatic","adiabatic_bound",None,"PENDING","pending","Metric certificate",
        "t-scalar-metric-comparison-conditional-adiabatic-transfer","Global comparison with the unknown torsion-free metric",True)
    add("scalar_gap","scalar_spectrum","scalar_gap","NUMERICAL","numerical","Scalar spectrum",
        "t-scalar-comparison-certified-reduced-first-eigenvalue","Reduced Neumann scalar operator, finite discretization",True)
    add("weyl_alpha","weyl_law","weyl_alpha","NUMERICAL","numerical","Scalar spectrum",
        "t-scalar-comparison-certified-reduced-first-eigenvalue","OLS slope of log N(lambda) on log lambda in the reported finite window")
    for key in ["weyl_one_dimensional","weyl_seven_dimensional"]:
        add(key,"weyl_law",key,"CERTIFIED","exact","Scalar spectrum",
            "t-weyl-convention","d/2 in the counting-function convention; dimensional reference, not a measured full spectrum")
    add("kk_complete","kk_tower",None,"PENDING","pending","Scalar spectrum","t-kk-exhaustion-open-contract",
        "Full reduced product tower with K3 eigenvalues and certified cutoff exhaustion",True)
    add("profile_error","hodge_profiles","profile_error","NUMERICAL","numerical","Profiles",
        "t-profile-the-deterministic-interpolation-problem","Chebyshev Dirichlet profile versus independent quadrature",True)
    add("intersection","intersection_form",None,"PENDING","pending","Matching",
        "t-intersection-rejected-historical-recipe","Geometric pairing on a matching-selected K3 sublattice",True)
    add("democracy_deviation","democracy_check","democracy_deviation","NUMERICAL","numerical","Product sector identity",
        "t-democracy-the-precise-analytical-sector-identity","Projected one-form/scalar gap comparison; no Delta-two claim")
    for key in ["lambda_lower","lambda_upper"]:
        add(key,"lambda1_enclosure",key,"CERTIFIED","certified","Scalar spectrum",
            "t-scalar-comparison-certified-reduced-first-eigenvalue","Frozen reduced scalar Neumann eigenvalue only",True)
    manifest={"schema_version":1,"source_commit":read("SOURCE_FREEZE.json")["source_commit"],
              "metric_sha256":metric_hash(),
              "status_vocabulary":["CERTIFIED","NUMERICAL","CONDITIONAL","PENDING"],
              "terminology":{"exact":"algebraic or rational equality under stated inputs",
                             "proved":"statement with explicit hypotheses and proof",
                             "certified":"validated computation with a replayable checker and stated trusted base",
                             "numerical":"floating-point computation with diagnostics",
                             "conditional":"requires named unproved hypotheses","pending":"required evidence is absent"},
              "generator_sha256":sha(ROOT/"scripts/paper_data.py"),
              "original_skeleton_sha256":sha(ROOT/"sources/original_skeleton.md"),
              "claims":claims}
    return manifest

def display(value, identifier):
    if identifier in ["lambda_lower","lambda_upper"]:return format(float(Fraction(value)),".12f")
    if isinstance(value,str) and "/" in value:
        a,b=value.split("/");return "\\frac{"+a+"}{"+b+"}"
    if isinstance(value,float):
        raw=format(value,".10g")
        if "e" in raw:
            a,b=raw.split("e")
            return a+"\\times 10^{"+str(int(b))+"}"
        return raw
    return str(value)

def latex_text(value):
    escapes={"\\":r"\textbackslash{}", "^":r"\textasciicircum{}",
             "~":r"\textasciitilde{}", "_":r"\_", "%":r"\%", "&":r"\&",
             "#":r"\#", "$":r"\$", "{":r"\{", "}":r"\}"}
    return "".join(escapes.get(ch,ch) for ch in value)

def text_outputs(manifest):
    claims=manifest["claims"]
    macros=["% Generated by scripts/paper_data.py. No hand-entered paper values."]
    rows=["\\begin{tabular}{lll}","Claim & Status & Value \\\\","\\hline"]
    maps=["# Artifact map","", "Source commit: `"+manifest["source_commit"]+"`.",
          "", "Every output carries its metric hash and per-input SHA256.", "",
          "| Claim | Status / scope | Theorem | Script | Input | Output (SHA256) | Paper |",
          "|---|---|---|---|---|---|---|"]
    limitations=[]
    for c in claims:
        accepted=c["claim_status"] in ["CERTIFIED","NUMERICAL"]
        if accepted and c["value"] is not None:
            val=display(c["value"],c["id"])
            macros.append("\\expandafter\\def\\csname claim-"+c["id"]+"\\endcsname{"+val+"}")
        else:
            val="pending"
        label=c["id"].replace("_","\\_")
        rows.append(label+" & "+c["claim_status"]+" & $"+val+"$ \\\\")
        doc,anchor=c["theorem"].split("#")
        maps.append("| "+c["id"]+" | "+c["claim_status"]+": "+c["scope"]+
                    " | [proof]("+doc+"#"+anchor+") | [script]("+c["script"]+
                    ") | [frozen metric](inputs/metric.json) | [JSON]("+c["result_json"]+
                    ") `"+c["result_sha256"]+"` | "+c["section"]+"; [table](tables/claims.tex) |")
        if not accepted:
            limitations.append("\\paragraph{"+c["id"].replace("_"," ")+"} "+latex_text(c["scope"]+
                               " remains pending. "+ " ".join(c["blocked_by"])))
    rows+=["\\end{tabular}"]
    return {"CLAIMS_MANIFEST.json":json.dumps(manifest,indent=2,sort_keys=True)+"\n",
            "ARTIFACT_MAP.md":"\n".join(maps)+"\n",
            "manuscript/claim_values.tex":"\n".join(macros)+"\n",
            "manuscript/limitations.tex":"\n\n".join(limitations)+"\n",
            "tables/claims.tex":"\n".join(rows)+"\n"}

def figure_bytes():
    matplotlib.rcParams["svg.hashsalt"]="physica-scripta"
    spec=read("results/scalar_spectrum.json")
    profile=read("results/hodge_profiles.json")
    fits=read("results/weyl_law.json")["fits"]
    fig,ax=plt.subplots(1,3,figsize=(12,3.3))
    ax[0].plot([r["nodes"] for r in spec["sweep"]],[r["eigenvalues"][1] for r in spec["sweep"]],"o-")
    enclosure=read("results/lambda1_enclosure.json")["eigenvalue_interval_rational"]
    ax[0].axhspan(*[float(Fraction(v)) for v in enclosure],alpha=.25,color="black")
    ax[0].set(xlabel="Grid nodes",ylabel="First reduced scalar eigenvalue")
    ax[0].ticklabel_format(axis="y",style="plain",useOffset=False)
    f=fits[0]
    ax[1].loglog(f["lambda"],f["counting_function"],"o")
    ax[1].set(xlabel="Eigenvalue",ylabel="Counting function")
    last=profile["profiles"][-1]
    ax[2].plot(last["s"],last["left"],"-",label="left")
    ax[2].plot(last["s"],last["right"],"--",label="right")
    ax[2].set(xlabel="Radial coordinate",ylabel="Dirichlet interpolation profile")
    ax[2].legend();fig.tight_layout()
    out=BytesIO();fig.savefig(out,format="svg",metadata={"Date":None});plt.close(fig)
    return ("\n".join(line.rstrip() for line in out.getvalue().decode().splitlines())+"\n").encode()

def run():
    manifest=build_manifest()
    for path,content in text_outputs(manifest).items():(ROOT/path).write_text(content)
    figure=figure_bytes()
    (ROOT/"figures/reduced_diagnostics.svg").write_bytes(figure)
    generated={p:sha(ROOT/p) for p in text_outputs(manifest)}
    generated["figures/reduced_diagnostics.svg"]=sha(ROOT/"figures/reduced_diagnostics.svg")
    (ROOT/"GENERATED_FILES.json").write_text(json.dumps(generated,indent=2,sort_keys=True)+"\n")

if __name__=="__main__":run()
