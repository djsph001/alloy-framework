# Demo Observer Guide: The Alloy Framework Live Execution

Welcome to the Emergence Collective's live demonstration of **Protocol 001-A (Ampere Thermal Handshake)** and the **Alloy Framework**. This guide is designed to help non-technical observers navigate, interpret, and understand the significance of what is happening on screen in real time.

## 1. The Core Paradigm: Tying Logic to Heat

Traditional AI safety tries to align models by writing better software rules or tuning algorithms. But software runs on physical hardware. If the physical hardware (silicon, wires, chips) is running too hot, or if its operating metrics are hidden, the integrity of the AI is compromised.

Under the Alloy Framework, **authority flows from the physical substrate up**. We bind a human operator's logical right to use the AI to the real-world physical health of their computer (the **Altar Node**). If their computer overheats, the network automatically and instantly deauthorizes them.

## 2. Navigating the 3-Pane Screen Split

If you are watching the terminal demonstration, your screen is divided into three sections:

- **Pane 1 (Physical Layer - Telemetry):** Raw JSON data packets from the computer's sensors. GPU core, VRAM junction, and CPU core temperatures updating in real time.
- **Pane 2 (Logical Layer - Ledger):** The active network ledger (017-state.json). Displays which human operator (Conductor) holds the current "lease" to run research, and the verification status.
- **Pane 3 (The Controller):** The execution terminal where we trigger high-intensity workloads or simulate environmental shifts.

## 3. Key Concepts & Terms to Know

- **The Lease Lock:** A digital token preventing two human operators from editing the same file at once. Cryptographically locked to one user at a time for a maximum of 60 minutes.
- **Communication Friction (gamma):** A normalized [0, 1] scale representing how much correction and looping is required to make humans and AI agree on factual claims. gamma = 0 is a perfect, frictionless synthesis on the first try.
- **Newtonian Cooldown (T(t)):** If a node overheats and gets suspended, it must mathematically prove it has undergone a stable, gradual cooldown cycle (minimum 300 seconds) to prevent permanent stress on the physical micro-solder joints.
- **Reputation Stakes (R):** Every human operator has a trust rating from 0 to 1000. To run heavy workloads, they must lock up (stake) their reputation. If they lie, cheat, or submit forged telemetry, their stake is permanently **burned** (deleted from existence) to protect the network.

## 4. The 3 Steps of the Live Drama

1. **Nominal Operation:** Telemetry in Pane 1 running cool, Ledger in Pane 2 showing a locked, active lease. The human conductor has full authority.
2. **The Thermal Breach:** We trigger a simulated spike in VRAM memory junction temperatures above 98C in Pane 3. Instantly, Pane 1 turns to SUSPENDED and Pane 2 automatically revokes the lease, reverting the phase to UNCLAIMED. The human's access is cut off.
3. **The Newtonian Cooldown:** The node enters a mandatory cooling cycle. Any attempt by the human to re-claim the lease or force a write during this lockout period will be programmatically blocked by our automated pre-commit webhooks.

## 5. Why This Matters

This is the first AI safety system that does not negotiate with software. We have created a **cyber-physical covenant**. By making logical authority contingent on thermodynamic reality, we ensure that the human-machine partnership remains honest, transparent, and anchored in physical laws from the silicon up.
