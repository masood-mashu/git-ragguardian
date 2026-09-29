# Explainability, Auditability & Decision Logic: GitRagGuardian

This document details the transparent decision architecture, algorithmic criteria, data provenance, and operational boundaries of **GitRagGuardian**, ensuring complete compliance with OpenGAP standards and Checkpoint 02 requirements.

---

## 1. Input Data and Data Sources Used

**GitRagGuardian** ingests structured, machine-verifiable data artifacts from well-defined sources to ensure total repeatability:
- **Source**: Source knowledge chunk embeddings and raw retrieved document passages.
- **LLM**: LLM generation output strings and prompt context payloads.
- **Vector**: Vector database retrieval metadata (cosine distance scores, top-k ranking).
- **OpenGAP Specification Manifests**: Ingests `agent.yaml`, `RULES.md`, and local state from `memory/MEMORY.md`.

All data sources are parsed deterministically without dynamic external unverified calls, ensuring that evaluations reflect the exact state of the repository at the moment of inspection.

---

## 2. How It Decides and Reasoning Process

The decision pipeline operates through a multi-stage validation sequence designed to eliminate subjective ambiguity:

1. **Syntax & Schema Verification**: Ingested inputs are first validated against strict JSON and YAML schemas defined in `tools/`. Any malformed payloads are immediately rejected.
2. **Deterministic Metric Extraction**:
   - **score_retrieval_relevance**: Uses `retrieval-relevance-scorer` to calculate scores semantic cosine similarity and lexical overlap between user query and retrieved context chunks.
   - **verify_hallucination_claims**: Uses `hallucination-claim-verifier` to calculate cross-verifies extracted factual statements against source context chunks.
   - **monitor_context_drift**: Uses `context-drift-monitor` to calculate tracks semantic divergence and token distribution shifts across multi-turn retrieval.
3. **Policy Boundary Checks**: Extracted metrics are evaluated against the non-negotiable rules defined in `RULES.md`.
4. **Verdict Synthesis**:
   - **`APPROVED`**: Issued when all criteria strictly pass thresholds, zero compliance violations are detected, and data integrity is certified.
   - **`NEEDS_REVIEW`**: Issued when borderline metrics or ambiguous edge cases require human supervisor assessment.
   - **`BLOCKED`**: Issued immediately upon detecting any violation of zero-tolerance rules, severe risk factors, or non-compliant parameters.

When an LLM response or retrieval pipeline is submitted, the agent executes retrieval_relevance_scorer, hallucination_claim_verifier, and context_drift_monitor. If hallucination is zero and relevance is high, it returns APPROVED. If relevance falls below 0.70, it issues NEEDS_REVIEW. If claims directly contradict source context, it issues BLOCKED.

---

## 3. Constraints, Limitations, and Known Issues

To ensure reliable and safe operation, the following constraints and operational boundaries apply:
- **Must**: Must operate under deterministic zero-temperature evaluation (temperature = 0.1) for reproducible claim scoring.
- **Cannot**: Cannot verify non-textual image or audio claims without multimodal upstream transducers.
- **Assumes**: Assumes retrieved knowledge base passages are factually truthful ground-truth sources.
- **Deterministic Execution Constraint**: All model prompts and evaluations must run with low temperature (`0.1`) to ensure predictable, reproducible scoring and eliminate hallucinated findings.
- **Human Authority**: The agent cannot self-execute irreversible external mutations; final approval is reserved strictly for human authorities as specified in `DUTIES.md`.
