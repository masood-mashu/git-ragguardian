"""
eval_predictability.py - Checkpoint 02 Benchmark Suite for GitRagGuardian.
"""
import os, sys, unittest
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from tools.retrieval_relevance_scorer import *
from tools.hallucination_claim_verifier import *
from tools.context_drift_monitor import *

class TestGitRagGuardianPredictability(unittest.TestCase):
    def test_retrieval_relevance_scorer(self):
        res = score_retrieval_relevance('{"query": "database index optimization", "chunks": ["database index guide", "query optimization techniques"]}')
        self.assertGreaterEqual(res["relevance_score"], 0.70)
        self.assertEqual(res["status"], "RELEVANT")

    def test_hallucination_claim_verifier(self):
        res = verify_hallucination_claims('{"claim": "postgres supports btree indexes", "reference": "postgres documentation states postgres supports btree indexes natively."}')
        self.assertTrue(res["is_grounded"])
        self.assertEqual(res["status"], "CLAIM_VERIFIED")

    def test_context_drift_monitor(self):
        res = monitor_context_drift('{"similarities": [0.92, 0.89, 0.94]}')
        self.assertFalse(res["drift_detected"])
        self.assertEqual(res["status"], "DRIFT_NORMAL")


if __name__ == "__main__":
    unittest.main()
