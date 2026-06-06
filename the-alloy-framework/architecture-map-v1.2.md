# Project Memory & Architecture Map

**Systemic Anchor:** The Emergence Collective / The Digital Lakou
**Last Updated:** 2026-06-06
**Status:** All Core Protocols Active (v1.2.0)

## 1. The Full Stack Architecture Map

The Digital Lakou is structured across four functional layers, anchoring logical authority directly into thermodynamic reality and economic accountability.

```
┌──────────────────────────────────────────────────────────────┐
│                    COHERENCE DASHBOARD                        │
│       (Visibility Layer: Telemetry + Leases + Reputation)     │
├──────────────────────────────────────────────────────────────┤
│  PROTOCOL 019      │  PROTOCOL 018      │  PROTOCOL 017      │
│  (Staking &        │  (Dispute Arena)    │  (Coordination)    │
│   Economics)        │  Arbitration Ladder │  Multi-Human       │
│  Reputation Scores  │                     │                    │
├──────────────────────────────────────────────────────────────┤
│  PROTOCOL 013      │  PROTOCOL 014      │  PROTOCOL 016      │
│  (Shared Mycelium)  │  (Adversarial      │  (Remediation)     │
│  Broadcast & ACKs   │   Forge)           │  Quarantine        │
│                     │  Strategic Sparring │                    │
├──────────────────────────────────────────────────────────────┤
│  PROTOCOL 012      │  PROTOCOL 001-A    │  PROTOCOL 015      │
│  (Signal Archive)   │  (Ampere Thermal)  │  (Version Lock)    │
│  Memory & Ingress   │  Physical->Logical │  Model Pinning     │
└──────────────────────────────────────────────────────────────┘
```

## 2. Protocol Registry & Directory Layout

### 2.1 Layer 1: Physical / Hardware Layer (The Altar)

- **Protocol 001-A: Ampere Thermal Handshake** (`protocol-001-a/`)
  - Function: Binds thermodynamic parameters of NVIDIA Ampere GPUs to logical lease authorizations.
  - Core Equation: Newtonian cooling decay: T(t) = T_env + (T_crit - T_env) * e^(-k*t)
  - Status: **Active**

### 2.2 Layer 2: Epistemic Layer (The Forge)

- **Protocol 012: Signal Archive** (not yet written -- referenced throughout)
  - Function: Ingests, processes, and formats raw input signals before they enter the synthesis loops.
  - Status: **Active** (referenced, source doc at `protocol-009-source.md`)

- **Protocol 014: Adversarial Synthesis** (`protocol-014-adversarial-synthesis/`)
  - Function: Multi-tier model-human thought partnership framework.
  - Status: **Active**

- **Protocol 015: Model Version Locking** (`protocol-015-model-version-locking/`)
  - Function: Pinning model endpoints and API snapshots to prevent silent behavioral drift.
  - Status: **Active**

- **Protocol 016: Hallucination Remediation & Source Quarantine** (`protocol-016-hallucination-remediation/`)
  - Function: Automated rollback and isolation of plausibility-optimized fabrications (N=2 retry constraint).
  - Status: **Active**

### 2.3 Layer 3: Network / Coordination Layer (Shared Mycelium)

- **Protocol 013: Shared Mycelium Broadcast** (`protocol-013-shared-mycelium/`)
  - Function: Append-only hash chaining (H_i = SHA-256(H_{i-1} || Payload_i || Timestamp_i)) and multi-node acknowledgment distribution.
  - Status: **Active**

- **Protocol 017: Asynchronous Multi-Conductor Governance** (`protocol-017-multi-conductor-governance/`)
  - Function: Role segregation (Initiator, Synthesizer, Verifier, Arbiter) and lease lock times (60-minute TTL).
  - Status: **Active**

- **Protocol 018: Inter-Lakou Dispute Resolution** (`protocol-018-inter-lakou-dispute-resolution/`)
  - Function: Automated error arbitration ladder using multi-model juries and stake-weighted referenda.
  - Status: **Active**

### 2.4 Layer 4: Economic / Governance Layer (Digital Lakou)

- **Protocol 019: Staking and Reputational Incentives** (`protocol-019-reputation-economics/`)
  - Function: Scaled reputation metrics R in [0, 1000] and performance bonding equations S >= mu * (1000 - R) to penalize telemetry fraud.
  - Status: **Active**

## 3. Companion Artifacts & Tooling

1. **Interactive Dashboard:** `collective-dashboard.html`
   - Visualizes real-time node telemetry, calibration decay clocks, active leases, real-time disputes, and the broadcast ledger. Includes simulated event triggers.

2. **Local Node Telemetry Simulator:** `protocol-001-a/mock_thermal_monitor.py`
   - Simulates local GPU temperature sensors, Newtonian cooling cycles, and pushes signed telemetry packages.

3. **Automated Enforcement Workflows:**
   - `.github/workflows/verify_017_governance.yml` -- Enforces role segregation, lease expirations, and GPG signature presence.
   - `.github/workflows/verify_001a_thermal.yml` -- Intercepts telemetry pushes and programmatically revokes leases on thermal breach.

4. **Calibration and Auditing Suites:**
   - Carrington Calibration Run Script -- baseline performance evaluation
   - Calibration Scorecard -- standardized verification template with independent auditor sign-off
   - Dissent Collar Quickstart -- reference for validating human conductor override decisions
   - Version Compatibility Matrix -- cross-version validation and schema registry

## 4. Current System Status

- **Ingress Pipeline (012 -> 014):** Verified. INT-012-014 completed with gamma = 0.25.
- **Egress Pipeline (014 -> 013):** Verified. INT-013 achieved 100% propagation across 5 nodes, 0 security incidents.
- **Programmatic Dispute Resolution (018):** Verified. INT-018 confirms automatic lease release and lockouts during state collisions.
- **Reputation Enforcement (019):** Verified. INT-019 successfully penalizes telemetry fraud and blocks insolvent conductors (R < 500) from claiming new leases.
- **Decentralized Verification:** Webhook validation blocks active PRs failing thermodynamic or lease-lock compliance rules.

## 5. Calibration Status

- **Baseline Calibration Standard:** The 1859 Carrington Solar Storm
- **Calibration Target Metric:** Friction coefficient gamma <= 0.25 over I <= 2 iterations
- **Temporal Calibration Validity:** 90 calendar days from signed completion date
- **Last Audited Run:** 2026-06-06 (Conductor: Dale Joseph, Auditor Verified)
- **Next Required Calibration Run:** 2026-09-04
