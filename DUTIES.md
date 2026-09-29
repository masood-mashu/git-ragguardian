# Separation of Duties (SOD) & Operational Boundaries

To ensure robust compliance, security, and verification, **GitRagGuardian** implements a strict tripartite Separation of Duties architecture.

---

### 1. Maker
* **Assigned Entity**: `GitRagGuardian Automation Engine`
* **Responsibilities**:
  * Evaluates document retrieval relevance, verifies generated claims against retrieved context, and monitors semantic drift.
  * Ingests raw repository data, configurations, and input artifacts.
  * Formulates candidate evaluations and structured recommendation summaries.
  * Records execution logs into `memory/audit.log`.

---

### 2. Checker
* **Assigned Entity**: `GitRagGuardian Verification & Policy Enforcer`
* **Responsibilities**:
  * Enforces factual grounding thresholds, validates cosine distance metrics, and asserts prompt-to-context fidelity.
  * Audits calculations, parameter boundary limits, and zero-tolerance rule compliance.
  * Asserts schema validity on all output manifests.
  * Issues preliminary assessment: `APPROVED`, `BLOCKED`, or `NEEDS_REVIEW`.

---

### 3. Approver
* **Assigned Entity**: `Senior AI Platform Lead / Lead Data Scientist (Reserved exclusively for human review).`
* **Responsibilities**:
  * Final sign-off authority for high-impact production actions.
  * Mandatory human oversight on security, legal, financial, or regulatory decisions.
  * Reviews unresolvable edge cases and policy override exceptions.
