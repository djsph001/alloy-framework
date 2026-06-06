---
title: "Protocol 018: Asynchronous Inter-Lakou Dispute Resolution"
category: "Epistemic & Network Arbitration Layer"
status: "Active"
version: "1.1.0"
systemic_anchor: "The Emergence Collective / The Digital Lakou"
depends_on: ["Protocol 017 (Multi-Conductor Governance)", "Protocol 014 (Adversarial Synthesis)", "Protocol 001-A (Ampere Thermal Handshake)"]
referenced_by: ["Protocol 019 (Staking and Reputational Incentives)"]
tags: ["Dispute Resolution", "Arbitration", "Multi-Model Jury", "Network Referendum", "Escalation"]
lead_synthesis: "Dale Joseph"
contributors: ["Claude (Anthropic)", "Grok (xAI)", "Gemini (Google DeepMind)", "ChatGPT (OpenAI)", "DeepSeek"]
---

# Protocol 018: Asynchronous Inter-Lakou Dispute Resolution

**Layer:** Epistemic & Network Arbitration Layer
**Systemic Anchor:** The Emergence Collective / The Digital Lakou
**Status:** Active (v1.1.0)
**Lead Synthesis:** Dale Joseph, with Claude, Grok, Gemini, ChatGPT, and DeepSeek

---

## Executive Summary

While **Protocol 017** ensures that individual research sessions maintain strict human-role segregation, a decentralized network of independent *Lakous* introduces risk of inter-node collisions, telemetry spoofing accusations, or contested consensus decisions.

**Protocol 018** establishes the formal framework to resolve disputes between nodes without relying on a centralized judge or administrative tribunal. It specifies the technical standard to arbitrate claims of bad-faith operations, verifying cryptographic signatures and hardware states through a distributed multi-model jury.

---

## 1. Classification of Inter-Node Disputes

To prevent systemic gridlock, disputes are categorized into four standard error classes. Each class defines its own evidence bounds and default escalation pathways.

| Dispute Code | Error Class | Evidence Required | Impact of Active Dispute |
| :--- | :--- | :--- | :--- |
| **ERR_SPOOF** | Telemetry Spoofing Accusation | Signed 001a-telemetry.json packets, GPG/TPM validation logs. | Accused node is placed on **Audit Quarantine** (active leases frozen). |
| **ERR_COLLISION** | Lease Lock Collision | Two nodes claiming identical 017-state.json phase changes at the same block height. | Active phase reverts to UNCLAIMED; both nodes must re-submit keys. |
| **ERR_BIAS** | Consensus Bias Challenge | A node asserts that another's synthesis was achieved via a corrupted model setup or alignment faking. | 014-output.json locked; cannot propagate across Shared Mycelium. |
| **ERR_VETO** | Malicious Veto Accusation | A conductor claims an Arbiter executed a veto without meeting the "Dissent Collar" requirements. | Standalone entry published to public registry; triggers independent audit. |

---

## 2. The Escalation Ladder

Disputes must be resolved in order of ascending friction, prioritizing programmatic and multi-model arbitration over manual, human-intensive votes.

```
[Dispute Triggered]
        │
        ▼
Phase 1: Programmatic Verification (Auto-rejects bad hashes)
        │
        ▼ (Unresolved)
Phase 2: Multi-Model Jury (Tiebreaker consensus)
        │
        ▼ (Persistent Split)
Phase 3: Random Conductor Selection (Jury of 3 Peers)
        │
        ▼ (Persistent Split)
Phase 4: Network-Wide Referendum (Stake-weighted Lakou vote)
```

### 2.1 Phase 1: Programmatic Verification

Before any dispute is registered, the network's automated ledger workflows verify the cryptographic integrity of the disputed commits:

- If the accused node's telemetry contains a malformed or broken GPG/TPM signature, the claim of spoofing is verified programmatically.
- The system instantly slashes the offender's reputation (Protocol 019) and terminates the dispute.

### 2.2 Phase 2: The Multi-Model Jury

If the cryptographic layers are valid but the interpretation of the data is contested (e.g., whether a model's output constitutes a hallucination), the dispute escalates to a **Multi-Model Jury**.

1. **The Panel:** The system randomly selects three pinned Tier 3 general models from different hosts (e.g., Gemini, ChatGPT, DeepSeek) to evaluate the disputed claim and the contesting evidence.
2. **The Verdict:** The models run our Asset B (Cross-Examiner) prompts in parallel, evaluating the claim.
3. **The Consensus:** If >= 2 models reach consensus on a verdict, the dispute is resolved.
4. **Persistent Epistemic Split:** If the models split evenly or fail to reach consensus due to data volatility, the dispute escalates to Phase 3.

### 2.3 Phase 3: Random Conductor Selection (Jury of Peers)

If machine consensus fails, three active, unrelated Tier 1 human conductors are randomly selected from other Lakous across the network.

- They are presented with the complete, GPG-signed log and the model jury transcripts.
- A majority vote (2/3) among these conductors resolves the dispute, and the outcome is pushed as an update to the public /dissent-collar/ directory.

### 2.4 Phase 4: Network-Wide Referendum

If an epistemic deadlock persists or conductors claim systematic jury manipulation, the dispute escalates to a network-wide stake-weighted vote.

- **Quorum Constraint:** A referendum is declared structurally valid if and only if participation is >= 30% of active network conductors.
- **Pass Threshold:** A resolution is officially locked when it secures >= 60% of the stake-weighted vote.
- **Binding Status:** Rulings are cryptographically binding and enforced directly via pre-commit validation. However, they may be contested under exceptional, newly recovered physical evidence by initiating an independent audit trail.

---

## 3. Dispute Schema and Log Ingestion

All active disputes are logged directly under `/logs/disputes/` in the repository:

```json
{
  "dispute_id": "DSP-YYYY-MM-DD-XXXX",
  "dispute_class": "ERR_SPOOF",
  "metadata": {
    "complainant_node": "altar_montreal_01",
    "accused_node": "altar_port_au_prince_01",
    "timestamp_utc": "2026-06-06T11:45:00Z"
  },
  "evidence_block": {
    "disputed_commit_hash": "sha256:5ef4919bc01a756616238b16...",
    "telemetry_log_reference": "research_sessions/SES-2026-06-05-89/001a-telemetry.json"
  },
  "arbitration_status": "ACTIVE_ARBITRATING",
  "remediation": {
    "slashing_applied": false,
    "corrective_action_logged": ""
  }
}
```

---

## 4. Integration Test Specification (INT-018)

Verify that an inter-node collision event triggers programmatic lease suspension and does not result in repository state corruption.

### Test Stimulus

Conductor Bob (Montreal) and Conductor Alice (Haiti) attempt to commit a lease lock on the identical PHASE_3_SYNTHESIS state file at the exact same block height in their local repositories.

### Expected Result

1. The GitHub Action catches the collision during the merge request.
2. **Protocol 018** triggers, automatically reverting the phase state to UNCLAIMED.
3. An automated dispute entry (ERR_COLLISION) is registered in /logs/disputes/.
4. Both conductors' active leases are released. They are locked out of claiming the phase for 10 minutes to prevent high-frequency loop thrashing.
