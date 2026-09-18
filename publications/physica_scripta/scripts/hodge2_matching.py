"""Exact product cohomology accounting; fail closed on absent boundary maps."""
from common import write_result

def run():
    # Kunneth convolution for K3 x T2 x I; I retracts to a point.
    k3 = [1,0,22,0,1]; torus = [1,2,1]
    product = [sum(k3[i]*torus[k-i] for i in range(len(k3))
                   if 0 <= k-i < len(torus)) for k in range(7)]
    write_result("hodge2_matching.json", {
        "status":"PENDING", "scope":"ordinary real cohomology of bare product neck",
        "k3_betti":k3, "torus_betti":torus, "product_betti":product,
        "values":{"product_h_two":product[2]}, "target":21,
        "matching_operator":None,"boundary_domain":None,"basis":None,
        "rank":None,"kernel_dimension":None,"action_on_H2_K3":None,
        "blocked_by":["Restriction maps from both ends and their identifications on H^2(K3) are absent.",
                      "Counting coordinate index pairs gives dim Lambda^2(R^7), not a Betti number.",
                      "Compact quotient lattice data from other branches does not define this neck boundary problem."]
    })

if __name__ == "__main__": run()
