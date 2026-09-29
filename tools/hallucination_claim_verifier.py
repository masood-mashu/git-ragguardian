"""
hallucination_claim_verifier.py - Cross-verifies extracted factual statements against source context chunks
"""
import sys
import json


def verify_hallucination_claims(claim_verification_json: str):
    import json
    data = json.loads(claim_verification_json) if isinstance(claim_verification_json, str) else claim_verification_json
    claim = data.get("claim", "").lower()
    ref = data.get("reference", "").lower()
    is_grounded = all(term in ref for term in claim.split() if len(term) > 4)
    return {"is_grounded": is_grounded, "hallucination_detected": not is_grounded, "status": "CLAIM_VERIFIED" if is_grounded else "HALLUCINATION_DETECTED"}


if __name__ == "__main__":
    print(json.dumps({"status": "READY", "tool": "hallucination-claim-verifier"}))
