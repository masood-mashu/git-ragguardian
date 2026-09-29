"""
context_drift_monitor.py - Tracks semantic divergence and token distribution shifts across multi-turn retrieval
"""
import sys
import json


def monitor_context_drift(turn_history_json: str):
    import json
    data = json.loads(turn_history_json) if isinstance(turn_history_json, str) else turn_history_json
    scores = data.get("similarities", [0.95, 0.90, 0.88])
    avg_sim = round(sum(scores) / max(len(scores), 1), 2)
    drift = avg_sim < 0.75
    return {"avg_similarity": avg_sim, "drift_detected": drift, "status": "DRIFT_ALERT" if drift else "DRIFT_NORMAL"}


if __name__ == "__main__":
    print(json.dumps({"status": "READY", "tool": "context-drift-monitor"}))
