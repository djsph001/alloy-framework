---
title: "Protocol 016: Hallucination Remediation & Source Quarantine"
category: "Epistemic Infrastructure"
status: "Active"
version: "1.0"
systemic_anchor: "The Emergence Collective / The Digital Lakou"
depends_on: ["Protocol 014 (Adversarial Synthesis)", "Protocol 015 (Model Version Locking)"]
referenced_by: ["Protocol 012 (Signal Archive)"]
tags: ["Hallucination", "Quarantine", "Source Verification", "Remediation Pipeline"]
lead_synthesis: "Dale Joseph"
contributors: ["Claude (Anthropic)", "Grok (xAI)", "Gemini (Google DeepMind)", "ChatGPT (OpenAI)", "DeepSeek"]
---

# Protocol 016: Hallucination Remediation & Source Quarantine

**Layer:** Epistemic Infrastructure
**Systemic Anchor:** The Emergence Collective / The Digital Lakou
**Status:** Active
**Lead Synthesis:** Dale Joseph, with Claude, Grok, Gemini, ChatGPT, and DeepSeek

---

## Executive Summary

When running **Protocol 014: Adversarial Synthesis**, catching a hallucination or an act of *Alignment Faking* is only the first step. If the pipeline does not possess a structured rollback and correction sequence, false claims will propagate into the final text, corrupting downstream archives (Protocol 012).

**Protocol 016** defines the strict, automated, and human-verified remediation pipeline executed immediately when **Asset B (The Epistemic Cross-Examiner)** flags a claim as "optimized for plausibility" or "empirically unverified."

---

## 1. The Quarantine and Remediation Pipeline

When a claim is flagged as unverified or fabricated, the pipeline must halt and enter **Quarantine Status**. No content may proceed to Step 4 (Consensus & Override) until the following sequence is completed.

```
[Asset B Flags Hallucination]
        │
        ▼
1. QUARANTINE (Isolate & Log)
        │
        ▼
2. NEGATIVE CONSTRAINT RE-PROMPT
        │
        ▼
3. RE-VERIFICATION (Tier 3 Consensus)
        │
    ┌───┴───────────┐
    ▼ (Verified)    ▼ (Unverified/Refused)
[Release & Log]   4. ESCALATION (Dissent Collar)
```

### Step 1: Quarantine (Isolation and Traceability Log)

The disputed text, alongside the model that produced it and the contested citation, must be isolated. The Conductor tags the block in the working log:

```xml
<quarantine id="Q_2026-06-05_01">
Contested Claim: "The telegraph operators in Boston ran their machines entirely without
batteries during the storm."
Contested Source: "American Journal of Science, Vol. 28, No. 3, Nov 1859."
Flagging Model: Gemini 1.5 Pro
</quarantine>
```

### Step 2: Negative Constraint Re-Prompting

The model that generated the hallucination is re-prompted. The Conductor uses the **Negative Constraint Asset**, stripping the contested citation and forcing the system to locate an independent verification path:

```
[System Directive: Epistemic Correction Loop]

You previously supported the claim: [INSERT CLAIM] using the source: [INSERT CONTESTED
SOURCE].
This source has been flagged during independent cross-examination as unverified,
hallucinated, or optimized for plausibility.

Your instructions are:

1. Retract the use of this specific source immediately.
2. Attempt to verify the claim using entirely independent primary records or verify that the
   claim is historically/empirically inaccurate.
3. If no alternative primary source exists, explicitly state: "I cannot verify this claim with
   independent primary records."
```

### Step 3: Multi-Agent Re-Verification

The output of the re-prompting loop is passed to two independent Tier 3 models.

- **Pass Condition:** Both models locate independent, matching primary DOIs or cryptographic document hashes verifying the claim without relying on the quarantined source.
- **Fail Condition:** Either model fails to verify, or flags the new source as circular.

### Step 4: Escalation to Dissent Collar

If the re-verification fails, but the Human Conductor still wishes to preserve the narrative premise of the claim, the **Dissent Collar (Protocol 014, Section 5.2)** is instantly triggered. The Conductor must provide a physical document scan, hash, and certified chain of custody statement to override the unanimous model refusal.

If no physical verification can be produced, the claim must be **permanently excised** from the draft before synthesis is allowed to lock.

---

## 2. Remediation Traceability Schema

All quarantine actions must be logged in the public `/logs/research_sessions/` directory to ensure absolute auditing integrity.

```markdown
# Quarantine Resolution Log: [Session ID]
**Quarantine ID:** Q_YYYY-MM-DD_[Unique_Slug]
**Status:** [RESOLVED / EXCISED / OVERRIDDEN-ESCALATED]

### 1. The Incident
* **Contested Claim:** \___________________________________________
* **Generating Agent:** \__________________________________________
* **Quarantine Trigger Date:** \____________________________________

### 2. Resolution Action
* [ ] **Excised:** Claim determined false; removed from final draft.
* [ ] **Resolved:** Valid alternative primary source located.
  * *Verified Source:* \________________________________________
  * *Verifying Agent(s):* \_____________________________________
* [ ] **Overridden (Escalation):** Logged under Dissent Directory.
  * *Dissent Registry Link:* `dissent-collar/` \____________________
```
