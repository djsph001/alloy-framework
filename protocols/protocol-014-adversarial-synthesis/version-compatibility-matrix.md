---
title: "Version Compatibility & Calibration Validity Matrix"
parent: "Protocol 014: Adversarial Synthesis"
type: "Companion Document — Interface Contract"
version: "1.0"
core_reference: "Protocol 014 (Adversarial Synthesis)"
---

# Version Compatibility & Calibration Validity Matrix

**Parent Layer:** Epistemic Infrastructure
**Core Reference:** Protocol 014 (Adversarial Synthesis)
**Status:** Active

---

## 1. Cross-Version Integrity Matrix

To prevent schema drift across the pipeline, all outputs passed from the **Forge (014)** to downstream storage in the **Signal Archive (012)** or broadcasting via the **Shared Mycelium (013)** must comply with the following structural interface.

| Protocol Source | Input Schema Interface | Output Schema Interface | Target Version | Status |
| :--- | :--- | :--- | :--- | :--- |
| 012 (Signal Archive) | N/A (Raw Inference Log) | 014-input.json | v1.0.0 | Locked |
| 014 (Adversarial Synthesis) | 014-input.json | 014-output.json | v1.1.0 | Active |
| 013 (Shared Mycelium) | 014-output.json | broadcast.msg | v0.9.0-draft | In Dev |

### Schema Verification Hashes

- **014-input.schema.json Hash:**
  SHA-256: `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855`

- **014-output.schema.json Hash:**
  SHA-256: `f83ac7130b2b814a6015b0f00a08d2feaa0c55ad015a3bf4f1b2b0b822cd15d`

---

## 2. Calibration Expiry and Recalibration Intervals

To account for human cognitive habituation and silent API parameter modifications by host providers, the **Carrington Calibration Status** is subject to a strict decay function.

```
[Carrington Pass] ──► Valid for 90 Days
        │
    ┌───┴───────────────────┐
    ▼ (Any trigger below)   ▼ (90 Days Elapsed)
[Recalibration Triggered]   [Calibration Expired]
    │                       │
    └───────┬───────────────┘
            ▼
    [Run Carrington Protocol 014]
```

### Recalibration Triggers

A team's passing status on the Carrington Scorecard is immediately invalidated, requiring a fresh calibration run, if any of the following conditions are met:

1. **Temporal Expiry:** Ninety (90) calendar days have elapsed since the last signed and audited Carrington Calibration Run.

2. **Model Set Drift:** Any model within the active Tier 2 or Tier 3 configuration undergoes a version bump, transition to a new base API snapshot, or backend weight update (as defined in Protocol 015).

3. **Conductor Shift:** The designated Tier 1 Human Conductor changes, or a new co-conductor is introduced to the pipeline.

4. **Operational Friction Spike:** The running average of communication friction (gamma) across three consecutive research sessions exceeds gamma = 0.50.
