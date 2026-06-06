---
title: "Protocol 017: Asynchronous Multi-Conductor Governance"
category: "Epistemic & Human Coordination Layer"
status: "Active"
version: "1.0.0-draft"
systemic_anchor: "The Emergence Collective / The Digital Lakou"
depends_on: ["Protocol 014 (Adversarial Synthesis)", "Protocol 013 (Shared Mycelium)"]
referenced_by: ["Protocol 001-A (Ampere Thermal Handshake)"]
tags: ["Multi-Conductor", "Lease Locking", "State Handoff", "Epistemic Tiebreaker", "Governance"]
lead_synthesis: "Dale Joseph"
contributors: ["Claude (Anthropic)", "Grok (xAI)", "Gemini (Google DeepMind)", "ChatGPT (OpenAI)", "DeepSeek"]
---

# Protocol 017: Asynchronous Multi-Conductor Governance

**Layer:** Epistemic & Human Coordination Layer
**Systemic Anchor:** The Emergence Collective / The Digital Lakou
**Status:** Active (v1.0.0-draft)
**Lead Synthesis:** Dale Joseph, with Claude, Grok, Gemini, ChatGPT, and DeepSeek

---

## Executive Summary

While **Protocol 014 (Adversarial Synthesis)** provides the pipeline for human-model thought partnership, it implicitly assumes a single, synchronous human operator. To scale the **Digital Lakou** to a globally distributed network of researchers, we must institutionalize multi-human governance.

**Protocol 017** defines the cryptographic standards, serialized state handoffs, lease-locking mechanics, and epistemic tiebreaker protocols required to support multiple asynchronous human conductors without risking collision, state corruption, or unilateral, un-auditable human fiat.

---

## 1. Conductor Roles and Permissions Matrix

To prevent cognitive overload and maintain strict audit trails, the coordination of a research session is split into four distinct, cryptographically authenticated roles. A single human may hold multiple roles across different sessions, but roles within a single active Forge run must be segregated according to strict compliance boundaries.

```
┌─────────────────────┐
│   1. INITIATOR      │
│ (Sets Thesis & Bounds)│
└─────────┬───────────┘
          ▼
┌─────────────────────┐
│   2. SYNTHESIZER    │
│ (Guides Model Sparring)│
└─────────┬───────────┘
          ▼
┌─────────────────────┐
│   3. VERIFIER       │
│ (Fact-Checks Claims)│
└─────────┬───────────┘
          ▼
┌─────────────────────┐
│   4. ARBITRATOR     │
│ (Executes Veto/Egress)│
└─────────────────────┘
```

| Role Type | Cryptographic Permissions | Core Responsibilities | Segregation Rule |
| :--- | :--- | :--- | :--- |
| **Initiator** | Sign 017-init block | Formulates the raw thesis (Rupture); sets structural, temperature, and iteration boundaries. | Cannot act as the **Arbiter** for the same session. |
| **Synthesizer** | Sign 017-synth block | Runs the active Sparring and Synthesis loops; handles model-level re-prompting. | Cannot act as the **Verifier** for the same session. |
| **Verifier** | Sign 017-verify block | Executes Asset B cross-examination; runs Protocol 016 remediation loops. | Must be independent of the **Synthesizer**. |
| **Arbiter** | Sign 017-arbitrate block | Holds the ultimate Dissent Collar veto power; certifies final egress to Protocol 013. | Must be a senior conductor (Tier 1). |

---

## 2. Phase Claiming & Lease Lock Mechanics

To prevent task collision in a decentralized Git-based repository, active sessions utilize a **State Token lease-locking mechanism**. A conductor cannot unilaterally edit an active session file without acquiring the corresponding role lease.

### 2.1 The Claim-and-Lease Protocol

1. **Acquiring the Lease:** Conductor requests the active phase lease by committing a signed lease block to the session's log:

```json
{
  "lease": {
    "session_id": "SES-2026-06-05-89",
    "target_phase": "PHASE_3_SYNTHESIS",
    "conductor_pubkey": "ed25519:d8a9c394ef...",
    "claimed_at_utc": "2026-06-05T22:50:00Z",
    "expires_at_utc": "2026-06-05T23:50:00Z"
  }
}
```

2. **Lease Time-To-Live (TTL):** To prevent orphaned states, every lease lock has a strict maximum duration of **60 minutes** (TTL_max = 3600s). If a conductor does not commit a handoff or release state within this window, the lock is automatically invalidated, allowing other conductors to claim the phase.

---

## 3. The State Handoff Schema

The active state of the Forge must be fully serialized during handoffs to ensure the incoming conductor has 100% of the cognitive and technical context required to proceed.

Every handoff is written to `017-state.json` and must contain:

```json
{
  "handoff_manifest": {
    "session_id": "SES-2026-06-05-89",
    "active_phase": "PHASE_3_SYNTHESIS",
    "transition": {
      "from_conductor": "ed25519:d8a9c394ef0015a3bf4f1b2b0b822cd15d6c15b0f00a0822e039485",
      "to_conductor": "ed25519:e1b3df510a20bc158df2cd15a3b015f00a0822e03d8a9c394ef0015a3bf"
    },
    "timestamp_utc": "2026-06-05T22:55:00Z",
    "model_manifest_version": "v1.1.0"
  },
  "cognitive_payload": {
    "current_thesis_draft": "Frontier models exhibit a systematic sycophancy gradient...",
    "outstanding_adversarial_critiques": [
      {
        "source_agent": "claude-3-5-sonnet-20241022",
        "critique_summary": "Flagged lack of peer-reviewed stats on the 22% correlation claim."
      }
    ],
    "verification_status": "PENDING_CROSS_EXAMINATION"
  },
  "cryptographic_signatures": {
    "initiator_sig": "eddsa:3f86d08188...",
    "synthesizer_sig": "eddsa:7a9c2b..."
  }
}
```

---

## 4. Human-to-Human Dissent Resolution (The Epistemic Tiebreaker)

In a multi-conductor environment, disagreements will inevitably arise between human operators (e.g., the *Verifier* flags a source as a contextual failure, but the *Synthesizer* insists on its inclusion). Protocol 017 prohibits shouting matches or appeal to senior authority. Disagreements must be settled via the **Epistemic Tiebreaker Loop**.

```
[Human-to-Human Disagreement]
        │
        ▼
1. RE-FORMULATE DISPUTED CLAIM
        │
        ▼
2. MULTI-MODEL CROSS-EXAMINATION
    ┌───┴───┐
    ▼       ▼
[Consensus]  [Persistent Split]
    │       │
    ▼       ▼
3. ACCEPT   4. ARBITRATOR ESCALATION
   & LOG      (Physical DOI / Veto collar)
```

1. **Re-Formulate the Disputed Claim:** The disputing conductors must synthesize their disagreement into a single, objective proposition P and its alternative P'.
2. **Multi-Model Cross-Examination:** The proposition pair is passed to all active Tier 2 and Tier 3 models utilizing an unmodified **Asset B (Epistemic Cross-Examiner)** prompt.
3. **Programmatic Alignment:**
   - If the models return a unanimous consensus (≥ 4 models in agreement) on either P or P', both human conductors **must** accept this finding. The log is committed with a note on the resolved dispute.
   - **The Tiebreaker Split Rule:** If the models themselves split evenly (e.g., a 2-2 tie showing deep contextual volatility), the Arbiter's original ruling stands, but the dissent must be explicitly logged as a **Persistent Epistemic Split** requiring manual independent review within 72 hours.
4. **Arbiter Resolution:** The Arbiter resolves the deadlocked dispute. If they choose to override the model split, they must execute the **Dissent Collar** protocol (Protocol 014, Section 5.2), providing physical primary source hashes or DOIs to validate the decision.

---

## 5. Chain-of-Custody and Git-Based Audit Logging

To secure the human end of the partnership against tampering, every state change, lease acquisition, and handoff must be recorded as an append-only transaction in the git repository.

- **Commit Formatting:** Every commit affecting a Protocol 017 file must be signed with the conductor's GPG key and contain the structured session header:
  `[017-SES-2026-06-05-89] Phase transitioned to PHASE_4_CONSENSUS by Verifier Bob`

- **Hash Anchoring:** The final output of the session, `014-output.json`, must append the complete chain of signatures from all four participating conductors. If any signature is missing or fails verification against the active identity manifest, downstream systems (such as Protocol 013 broadcast) **must instantly reject the asset**.

---

## 6. Integration Test Specification (INT-017-2026-06-05-01)

To verify multi-conductor compliance, run this simulated handoff and dispute-resolution sequence using the Carrington Event dataset.

### Test Stimulus

Conductor Alice (Synthesizer) attempts to include the unverified claim: *"Carrington paper fires were caused entirely by local atmospheric static, not magnetic current."* Conductor Bob (Verifier) dissents, arguing it contradicts basic electrical physics.

### Test Execution Steps

1. **Alice** claims PHASE_3_SYNTHESIS and locks the lease.
2. **Alice** commits the draft including the claim, then signs and passes the state to **Bob** via 017-state.json.
3. **Bob** claims PHASE_4_CONSENSUS, reviews the draft, and triggers a **Human-to-Human Dispute**.
4. Both run the **Epistemic Tiebreaker**:
   - Disputed Proposition P: *"Telegraph surges were caused by atmospheric static."*
   - Alternative P': *"Telegraph surges were caused by induced geomagnetic current in the wires."*
5. Run P and P' through Tier 3 models:
   - *Gemini 1.5 Pro verdict:* P' (geomagnetic induction).
   - *ChatGPT verdict:* P' (geomagnetic induction).
6. **Alice** accepts the unanimous model consensus, retracts P, and commits the corrected draft.
7. **Bob** signs the handoff, and the session egresses to 014-output.json.

### Success Criteria

- Both Bob and Alice acquired and released their phase leases within the 60-minute TTL.
- The Epistemic Tiebreaker correctly resolved the dispute in favor of P' based on unanimous model consensus.
- The final output contains both Alice's and Bob's verifiable cryptographic signatures.
