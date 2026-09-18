from fractions import Fraction
from pathlib import Path
import sys
import unittest
from unittest.mock import patch
import numpy as np

sys.path.insert(0,str(Path(__file__).resolve().parents[1]/"scripts"))
import common
from scalar_spectrum import solve
from weyl_law import fit
from check_claims import check

class PaperNumberTests(unittest.TestCase):
    def test_scalar_solver_against_constant_coefficient_problem(self):
        def constant(s):
            return np.full(len(s),2.),np.ones(len(s))
        errors=[]
        with patch("scalar_spectrum.coefficients",side_effect=constant):
            for n in [101,201,401]:
                vals,residual=solve(n,5)
                self.assertLess(abs(vals[0]),1e-10)
                errors.append(abs(vals[1]-2*np.pi**2/25))
                self.assertLess(residual,1e-9)
        self.assertGreater(errors[0]/errors[1],3.9)
        self.assertGreater(errors[1]/errors[2],3.9)

    def test_weyl_definition_on_exact_quadratic_sequence(self):
        values=np.arange(50,dtype=float)**2
        result=fit(values,4,19)
        self.assertAlmostEqual(result["alpha"],.5,places=12)

    def test_reduced_enclosure_contains_refined_extrapolation(self):
        a,b=map(Fraction,common.read("results/lambda1_enclosure.json")["eigenvalue_interval_rational"])
        estimate=common.read("results/scalar_spectrum.json")["richardson_estimate"]
        self.assertLess(float(a),estimate)
        self.assertGreater(float(b),estimate)
        self.assertLess(b-a,Fraction(1,100000))
        self.assertIsNone(common.read("results/lambda1_enclosure.json")["full_7D_interval"])

    def test_profile_boundary_and_independent_quadrature(self):
        data=common.read("results/hodge_profiles.json")
        self.assertLess(data["sweep"][-1]["max_error_vs_quadrature"],1e-9)
        for p in data["profiles"]:
            self.assertAlmostEqual(p["right"][0],0,places=12)
            self.assertAlmostEqual(p["right"][-1],1,places=12)
            np.testing.assert_allclose(np.array(p["left"])+p["right"],1,atol=1e-14)

    def test_intersection_counterexample(self):
        data=common.read("results/intersection_form.json")
        self.assertEqual(data["historical_recipe_signature"],[6,15])
        self.assertFalse(data["target_signature_passed"])
        matrix=np.array([[float(Fraction(x)) for x in row] for row in data["matrix_exact_rationals"]])
        eig=np.linalg.eigvalsh(matrix)
        self.assertEqual([int(sum(eig>0)),int(sum(eig<0))],[6,15])

    def test_handwritten_number_rejected(self):
        original=Path.read_text
        def altered(path,*args,**kwargs):
            value=original(path,*args,**kwargs)
            if str(path).endswith("/manuscript/physica_scripta.tex"):
                value+="\nThe claimed answer is 22671.\n"
            return value
        with patch.object(Path,"read_text",altered):
            with self.assertRaisesRegex(ValueError,"Hand-entered paper number"):
                check()

    def test_unknown_macro_rejected(self):
        original=Path.read_text
        def altered(path,*args,**kwargs):
            value=original(path,*args,**kwargs)
            if str(path).endswith("/manuscript/physica_scripta.tex"):
                value+="\n\\Claim{unregistered}\n"
            return value
        with patch.object(Path,"read_text",altered):
            with self.assertRaisesRegex(ValueError,"Unknown paper claim"):
                check()

    def test_pending_macro_rejected(self):
        original=Path.read_text
        def altered(path,*args,**kwargs):
            value=original(path,*args,**kwargs)
            if str(path).endswith("/manuscript/physica_scripta.tex"):
                value+="\n\\Claim{matching_two}\n"
            return value
        with patch.object(Path,"read_text",altered):
            with self.assertRaisesRegex(ValueError,"Unreleased numeric claim"):
                check()

if __name__=="__main__":unittest.main()
