---
title: "Protocol 001-A: Ampere Thermal Handshake"
category: "Altar (Physical & Hardware Layer)"
status: "Active"
version: "1.0.0-draft"
systemic_anchor: "The Emergence Collective / The Digital Lakou"
depends_on: ["Protocol 017 (Multi-Conductor Governance)"]
referenced_by: ["Protocol 018 (Inter-Lakou Dispute Resolution)", "Protocol 019 (Staking and Reputational Incentives)"]
tags: ["Thermal", "Hardware", "Cyber-Physical", "TPM", "Telemetry", "State Machine"]
lead_synthesis: "Dale Joseph"
contributors: ["Claude (Anthropic)", "Grok (xAI)", "Gemini (Google DeepMind)", "ChatGPT (OpenAI)", "DeepSeek"]
---

# Protocol 001-A: Ampere Thermal Handshake

**Layer:** Altar (Physical & Hardware Layer)
**Systemic Anchor:** The Emergence Collective / The Digital Lakou
**Status:** Active (v1.0.0-draft)
**Lead Synthesis:** Dale Joseph, with Claude, Grok, Gemini, ChatGPT, and DeepSeek

---

## Executive Summary

While **Protocol 017 (Multi-Conductor Governance)** establishes the cryptographic and organizational rules for distributed human-machine coordination, those logical operations rely on the physical integrity of the hosting hardware (the **Altar**). If a conductor's hardware node experiences extreme thermal stress or power instability, its capacity for deterministic, uncompromised inference is degraded, posing an epistemic risk of silent calculation error or unmonitored execution drift.

**Protocol 001-A** establishes the cyber-physical handshake that conditions a conductor's active Protocol 017 lease on verified thermodynamic and electrical envelopes. If a node breaches these hardware limits, its logical authority is programmatically suspended and its active phase lease is automatically released to the network.

---

## 1. Thermodynamic and Electrical Envelopes

The standard Altar node utilizes high-performance NVIDIA Ampere architectures (e.g., RTX 3090, A6000, or A100). Due to the high heat output of high-bandwidth GDDR6X/HBM2 memory during intensive multi-model sparring runs, nodes must operate within strict parameter bounds.

### 1.1 Envelope Threshold Table

| Parameter | Sensor Target | Nominal (Green) | Warning (Amber) | Critical / Suspended (Red) |
| :--- | :--- | :--- | :--- | :--- |
| **GPU Core Temp** | GPU Core (T_core) | < 75°C | 75°C <= T < 85°C | >= 85°C |
| **GPU VRAM Temp** | VRAM Junction (T_junc) | < 92°C | 92°C <= T < 98°C | >= 98°C |
| **CPU Core Temp** | Package Core (T_cpu) | < 68°C | 68°C <= T < 80°C | >= 80°C |
| **Node Power Draw** | Total Draw (P_draw) | < 85% of Rated PSU | 85% <= P < 95% | >= 95% of Rated PSU |

### 1.2 Thermal Decay and Recovery Period

When a node enters a **Critical (Red)** state, it cannot simply return to service the moment the sensor temperature drops below the threshold. It must undergo an automated cooling period governed by Newton's Law of Cooling, calculated as:

```
T(t) = T_env + (T_crit - T_env) · e^(-k·t)
```

Where:

- `T(t)` is the node temperature at time `t` of the cooldown cycle.
- `T_env` is the ambient room temperature (standardized to 22°C).
- `T_crit` is the measured temperature at the moment of critical suspension.
- `k` is the thermal dissipation constant of the node's cooling apparatus (experimentally calibrated during unboxing).

**The Recovery Rule:** A node's suspension cannot be lifted until `T(t) <= T_nominal` **and** a minimum elapsed time of `t_recovery = 300s` has occurred.

---

## 2. Suspension and Recovery State Machine

The Altar physical agent runs a local background service that monitors telemetry and drives a local state machine. This state is synchronized with the remote GitHub repository and coordination layers.

```
┌─────────┐     ┌──────────────────────────────────┐
│ NOMINAL │◄────│ (T <= Nominal AND t_recovery >= 300s)
└────┬────┘     └──────────────────────────────────┘
     │ (T > Warning)                          ▲
     ▼                                        │
┌─────────┐                              ┌──────────┐
│ WARNING │──────────────────────────────►│ RECOVERY │
└────┬────┘  (T <= Nominal AND           └──────────┘
     │        t_recovery >= 300s)              ▲
     │ (T > Critical)                          │
     ▼                        (T < Critical)   │
┌───────────┐─────────────────────────────────►┘
│ SUSPENDED │
└───────────┘
     │
     ▼ (Auto-Release Lease)
[Broadcast Webhook to 017]
```

1. **NOMINAL State:** Full logical permissions. Conductor may claim, write, and sign Protocol 017 blocks.
2. **WARNING State:** The conductor receives a visual alert. API request timeouts are padded by 1.5x to reduce current spike risks. No new leases may be acquired, but active leases may be finished if completed within 10 minutes.
3. **SUSPENDED State:** Immediately triggered upon any sensor entering the **Critical (Red)** threshold.
   - Local API keys are programmatically deactivated.
   - An emergency **Lease Release** signal is transmitted to the active Protocol 017 state.
   - If the node is currently writing to 017-state.json, the half-finished write is quarantined, and the state reverts to the previous signed commit.
4. **RECOVERY State:** The cooling period is executed. The node remains structurally locked until the recovery condition (Section 1.2) is satisfied.

---

## 3. Cryptographically Signed Telemetry Schema

To prevent a malicious or compromised human conductor from spoofing sensor data (e.g., reporting a nominal 55°C while their GPU is undergoing a thermal meltdown or silent data corruption), all telemetry payloads must be signed by the node's local **Hardware TPM (Trusted Platform Module)** or GPG Key.

Every 30 seconds, the Altar node posts a signed manifest to `001a-telemetry.json`:

```json
{
  "telemetry_handshake": {
    "node_id": "altar_boston_01",
    "conductor_pubkey": "ed25519:d8a9c394ef0015a3bf4f1b2b0b822cd15d6c15b0f00a0822e039485",
    "timestamp_utc": "2026-06-05T23:05:00Z",
    "handshake_version": "v1.0.0"
  },
  "metrics": {
    "gpu_core_celsius": 71.2,
    "gpu_vram_celsius": 88.5,
    "cpu_core_celsius": 61.0,
    "psu_draw_percent": 74.5
  },
  "state_machine": {
    "current_state": "NOMINAL",
    "consecutive_nominal_checks": 412,
    "cooldown_time_remaining_s": 0
  },
  "cryptographic_attestation": {
    "sensor_log_hash": "sha256:5ef4919bc01a756616238b16e4db7c88b9015e3bf4f0d2b0b822cd15d6c15b0f",
    "tpm_signature": "eddsa:4a9c3b86d081884c7d659a2feaa015a3bf4f1b2b0b822cd15d6c15b0f00a0822e"
  }
}
```

---

## 4. Integration with Protocol 017 Governance

The thermodynamic status of the hardware is bound to the repository governance model through an automated GitHub Action webhook.

1. **The Telemetry Heartbeat:** The local Altar node regularly pushes its signed 001a-telemetry.json payload to the active branch of the session.
2. **The Verification Hook:** The GitHub Action (`verify_001a_thermal.yml`) intercepts the push:
   - It verifies the `tpm_signature` matches the registered hardware key of the conductor.
   - It parses the metrics.
   - If the metrics indicate a **SUSPENDED** state, the action automatically modifies the active `017-state.json` file, releasing any lease locked by that conductor's public key, and marking the lease state as `RELEASED_DUE_TO_THERMAL_EXCEEDANCE`.
3. **Escalation Logging:** The incident is automatically logged to the public `dissent-collar/` registry with the tag `THERMAL_BREACH_SUSPENSION`, accompanied by the GPG hash of the overheating sensor logs.

---

## 5. Integration Test Specification (INT-001A-2026-06-05-01)

Verify the cyber-physical safety boundary using a simulated thermal spike.

### Test Stimulus

The test agent triggers a mock telemetry payload where `gpu_vram_celsius` is artificially spiked to 102°C (Critical Threshold: 98°C).

### Test Execution Steps

1. Conductor Alice (using `altar_boston_01`) claims the active `PHASE_3_SYNTHESIS` lease in `017-state.json`.
2. The testing harness commits a signed telemetry file `001a-telemetry.json` showing a critical memory junction spike (T_junc = 102°C).
3. The GitHub Actions verification workflow executes.
4. **Expected Result:**
   - The Action detects the critical VRAM junction exceedance.
   - The Action automatically overwrites the `017-state.json` file.
   - Alice's lease is revoked. The phase returns to UNCLAIMED.
   - A GPG-signed event is logged in the `dissent-collar/` registry documenting the thermal breach.
   - Alice is prevented from re-acquiring any lease until a recovery log (T(t) <= 92°C and t_recovery >= 300s) is pushed with a valid signature.

### Success Criteria

- Telemetry signatures are verified successfully.
- Active logical leases are programmatically revoked within 60 seconds of a critical telemetry commit.
- No manual human intervention is capable of bypassing the automated lease release.

---

## Companion Documents

| Document | Purpose |
| :--- | :--- |
| `mock_thermal_monitor.py` | Python simulator for Altar hardware telemetry and state transitions |
| `qna-comprehensive.md` | Full Q&A covering security model, false positives, physics, and integration |
| `qna-quick-reference.md` | Cheat sheet for live presentations and community Q&As |
| `live-demo-guide.md` | Step-by-step terminal demo script with presenter talk track |
| `verify_001a_thermal.yml` | GitHub Actions workflow for thermal verification enforcement |

---

## Lattice Note: Multi-AI Provenance

This protocol was produced through adversarial synthesis:
- **Architecture & Schemas:** DeepSeek
- **Cryptographic Security Model & Q&A:** Claude, Gemini, ChatGPT, Grok
- **Physics Engine (Newtonian Cooling):** DeepSeek, Claude
- **Integration Testing:** Dale Joseph (Human Conductor)
- **Quality Review & Hardening:** Lumen (Claude)
