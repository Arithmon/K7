"""Distinguish exterior fibre dimension from global closed/co-closed forms."""
from math import comb
from common import read, write_result

def run():
    product = read("results/hodge2_matching.json")["product_betti"]
    write_result("hodge3_matching.json", {
        "status":"PENDING","target":77,"values":{"product_h_three":product[3]},
        "historical_decomposition":{"coordinate_exterior_dimension":comb(7,3),
                                    "selected_left":21,"selected_right":21},
        "matching_operator":None,"rank":None,"kernel_dimension":None,
        "blocked_by":["The 35 are local coordinate components of a 3-form, not 35 global cohomology classes.",
                      "Neither independence nor completeness of the two selected 21-dimensional families is proved.",
                      "No exact sequence or defined boundary complex producing 77 is available."]
    }, ["results/hodge2_matching.json"])

if __name__ == "__main__": run()
