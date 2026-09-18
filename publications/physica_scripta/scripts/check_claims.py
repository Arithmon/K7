"""Fail on stale provenance, edited paper values, missing claims or open submission gates."""
import argparse
import json
import re
from common import ROOT, read, sha, validate_freeze, validate_result
from paper_data import RESULTS, build_manifest, text_outputs
from check_lambda1_enclosure import check as check_enclosure

def check(submission=False):
    validate_freeze()
    for name in RESULTS:validate_result("results/"+name+".json")
    check_enclosure(read("results/lambda1_enclosure.json"))
    manifest=read("CLAIMS_MANIFEST.json")
    if manifest!=build_manifest():raise ValueError("Manifest diverges from source computations or gate policy")
    for path,expected in text_outputs(manifest).items():
        if (ROOT/path).read_text()!=expected:raise ValueError("Edited or stale generated paper data: "+path)
    for path,digest in read("GENERATED_FILES.json").items():
        if sha(ROOT/path)!=digest:raise ValueError("Generated artifact changed: "+path)
    claims={c["id"]:c for c in manifest["claims"]}
    main=(ROOT/"manuscript/physica_scripta.tex").read_text()
    stripped=re.sub(r"(?m)%.*$","",main)
    stripped=stripped.replace(r"\newcommand{\Claim}[1]{\csname claim-#1\endcsname}", "")
    stripped=re.sub(r"\bK3\b", "", stripped)  # proper name, not a numerical claim
    if re.search(r"\d",stripped):
        raise ValueError("Hand-entered paper number: use a registered Claim macro")
    for identifier in re.findall(r"\\Claim\{([^}]+)\}",main):
        if identifier not in claims:raise ValueError("Unknown paper claim: "+identifier)
        c=claims[identifier]
        if c["claim_status"] not in ["CERTIFIED","NUMERICAL"] or c["value"] is None:
            raise ValueError("Unreleased numeric claim used by paper: "+identifier)
    # Generated numeric text is accepted only when its source and exact bytes agree.
    expected_includes={"claim_values","limitations","../tables/claims"}
    actual=set(re.findall(r"\\input\{([^}]+)\}",main))
    if actual!=expected_includes:raise ValueError("Untracked or missing manuscript input")
    open_claims=[c["id"] for c in claims.values() if c["submission_required"] and
                 c["claim_status"] not in ["CERTIFIED","NUMERICAL"]]
    if submission and open_claims:raise ValueError("Submission blocked: "+", ".join(open_claims))
    return open_claims

if __name__=="__main__":
    parser=argparse.ArgumentParser();parser.add_argument("--submission",action="store_true")
    args=parser.parse_args()
    pending=check(args.submission)
    print("Paper data consistent; open scientific gates: "+", ".join(pending))
