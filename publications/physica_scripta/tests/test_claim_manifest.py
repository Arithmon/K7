import copy
import json
from pathlib import Path
import sys
import tempfile
import unittest
from unittest.mock import patch

sys.path.insert(0,str(Path(__file__).resolve().parents[1]/"scripts"))
import common
from paper_data import build_manifest, text_outputs
from check_claims import check
from check_lambda1_enclosure import check as check_enclosure

class ManifestTests(unittest.TestCase):
    def test_live_manifest_and_provenance(self):
        self.assertEqual(common.read("CLAIMS_MANIFEST.json"),build_manifest())
        self.assertEqual(set(check()),{"nk","matching_two","matching_three","adiabatic","kk_complete","intersection"})

    def test_submission_remains_blocked(self):
        with self.assertRaisesRegex(ValueError,"Submission blocked"):
            check(submission=True)

    def test_frozen_source_byte_mutation_rejected(self):
        # A real byte mutation in an isolated fixture, no source-file edits.
        with tempfile.TemporaryDirectory(dir=common.ROOT) as tmp:
            p=Path(tmp);(p/"source.md").write_text("original")
            freeze={"files":[{"path":"source.md","sha256":common.sha(p/"source.md")}]}
            (p/"SOURCE_FREEZE.json").write_text(json.dumps(freeze))
            with patch.object(common,"ROOT",p),patch.object(common,"REPO",p):
                common.validate_freeze()
                (p/"source.md").write_text("mutated")
                with self.assertRaisesRegex(ValueError,"Frozen source changed"):
                    common.validate_freeze()

    def test_stale_producer_hash_rejected(self):
        original=common.sha
        def altered(path):
            return "0"*64 if str(path).endswith("/scripts/scalar_spectrum.py") else original(path)
        with patch.object(common,"sha",side_effect=altered):
            with self.assertRaisesRegex(ValueError,"Stale result dependency"):
                common.validate_result("results/scalar_spectrum.json")

    def test_interval_coverage_mutation_rejected(self):
        data=copy.deepcopy(common.read("results/lambda1_enclosure.json"))
        data["cells"][0]["domain"][0]="-1"
        with self.assertRaisesRegex(ValueError,"Incomplete domain"):
            check_enclosure(data)

    def test_interval_false_coefficient_bound_rejected(self):
        data=copy.deepcopy(common.read("results/lambda1_enclosure.json"))
        data["cells"][0]["g_inverse_ss"]=["1","2"]
        with self.assertRaisesRegex(ValueError,"Coefficient bound"):
            check_enclosure(data)

    def test_interval_false_final_bound_rejected(self):
        data=copy.deepcopy(common.read("results/lambda1_enclosure.json"))
        data["eigenvalue_interval_rational"]=["1","2"]
        with self.assertRaisesRegex(ValueError,"Incorrect eigenvalue"):
            check_enclosure(data)

    def test_pending_claim_has_no_numeric_macro(self):
        out=text_outputs(build_manifest())["manuscript/claim_values.tex"]
        for name in ["nk","matching_two","matching_three","adiabatic","kk_complete","intersection"]:
            self.assertNotIn("claim-"+name+"\\endcsname",out)

if __name__=="__main__":unittest.main()
