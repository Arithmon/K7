"""No K3 spectrum is replaced by four integer momenta."""
import json
from common import REPO, write_result

def run():
    old=json.loads((REPO/"publications/papers/notebooks/g2_spectral_companion_results.json").read_text())
    write_result("kk_tower.json",{
        "status":"PENDING","cutoff":20,"count":None,"full_metric_count_bracket":None,
        "historical_json_counts":old["results"]["kk_tower"],
        "excluded_modes_lower_bound":None,"complete":False,
        "exhaustion_contract":{
            "required_inputs":["certified K3 eigenvalue enclosures and multiplicities",
                               "torus periods and inverse metric", "radial boundary spectrum and coercivity bounds"],
            "criterion":"Every excluded radial or fibre mode must have a certified lower bound > cutoff.",
            "bracket_if_relative_error_delta_proved":"N_reduced(cutoff/(1+delta)) <= N_full(cutoff) <= N_reduced(cutoff/(1-delta))"},
        "blocked_by":["The old six-integer fibre sum treats four K3 directions as periodic flat coordinates.",
                      "A K3 spectrum with multiplicities and a certified tail bound is absent.",
                      "The archived result reports 1744 distinct/4460 with multiplicity, not 22671.",
                      "No justified full metric adiabatic error is available for cutoff bracketing."]
    })

if __name__ == "__main__": run()
