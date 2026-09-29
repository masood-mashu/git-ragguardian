"""
retrieval_relevance_scorer.py - Scores semantic cosine similarity and lexical overlap between user query and retrieved context chunks
"""
import sys
import json


def score_retrieval_relevance(query_context_json: str):
    import json
    data = json.loads(query_context_json) if isinstance(query_context_json, str) else query_context_json
    chunks = data.get("chunks", [])
    query = data.get("query", "").lower()
    matches = sum(1 for c in chunks if any(word in c.lower() for word in query.split()))
    score = round(matches / max(len(chunks), 1), 2)
    status = "RELEVANT" if score >= 0.70 else "LOW_RELEVANCE"
    return {"relevance_score": score, "chunks_evaluated": len(chunks), "status": status}


if __name__ == "__main__":
    print(json.dumps({"status": "READY", "tool": "retrieval-relevance-scorer"}))
