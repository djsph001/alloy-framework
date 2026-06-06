#!/usr/bin/env python3
"""
Protocol 001-A: Mock Thermal Monitor Simulator
Designed to simulate Altar hardware telemetry, write cryptographically signed
telemetry payloads, and test automated suspension state transitions.
"""

import json
import time
import random
import os

# Define mock environment
TELEMETRY_PATH = "research_sessions/SES-2026-06-05-89/001a-telemetry.json"
STATE_PATH = "research_sessions/SES-2026-06-05-89/017-state.json"

# Thermal thresholds
LIMIT_GPU_VRAM = 98.0
NOMINAL_GPU_VRAM = 92.0

class AltarNode:
    def __init__(self, node_id="altar_boston_01"):
        self.node_id = node_id
        self.gpu_core = 55.0
        self.gpu_vram = 80.0
        self.cpu_core = 48.0
        self.psu_draw = 60.0
        self.state = "NOMINAL"
        self.cooldown_remaining = 0

    def generate_metrics(self, spike=False):
        """Generates mock telemetry data, with an option to force a memory junction spike."""
        if spike:
            # Force critical thermal breach
            self.gpu_core = random.uniform(80.0, 86.0)
            self.gpu_vram = random.uniform(99.0, 104.0)
            self.cpu_core = random.uniform(72.0, 78.0)
            self.psu_draw = random.uniform(91.0, 97.0)
        else:
            if self.state == "RECOVERY":
                # Execute cooling simulation
                self.gpu_vram -= random.uniform(2.0, 4.0)
                self.gpu_core -= random.uniform(1.5, 3.0)
                self.cpu_core -= random.uniform(1.0, 2.0)
                if self.gpu_vram <= NOMINAL_GPU_VRAM:
                    self.gpu_vram = NOMINAL_GPU_VRAM
                    self.state = "NOMINAL"
                    print("[SIMULATOR] Cooldown complete. Node returned to NOMINAL status.")
            else:
                # Normal operational jitter
                self.gpu_core = random.uniform(62.0, 74.0)
                self.gpu_vram = random.uniform(82.0, 91.0)
                self.cpu_core = random.uniform(50.0, 65.0)
                self.psu_draw = random.uniform(55.0, 78.0)

        # Check limits
        if self.gpu_vram >= LIMIT_GPU_VRAM and self.state != "SUSPENDED":
            self.state = "SUSPENDED"
            print(f"[SIMULATOR] ALERT: VRAM Temperature Spiked to {self.gpu_vram:.1f}°C!")
            print("[SIMULATOR] Auto-releasing logical leases and transitioning to SUSPENDED state.")

    def export_telemetry(self):
        """Saves signed mock telemetry payload to disk."""
        os.makedirs(os.path.dirname(TELEMETRY_PATH), exist_ok=True)
        
        payload = {
            "telemetry_handshake": {
                "node_id": self.node_id,
                "conductor_pubkey": "ed25519:d8a9c394ef0015a3bf4f1b2b0b822cd15d6c15b0f00a0822e039485",
                "timestamp_utc": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
                "handshake_version": "v1.0.0"
            },
            "metrics": {
                "gpu_core_celsius": round(self.gpu_core, 1),
                "gpu_vram_celsius": round(self.gpu_vram, 1),
                "cpu_core_celsius": round(self.cpu_core, 1),
                "psu_draw_percent": round(self.psu_draw, 1)
            },
            "state_machine": {
                "current_state": self.state,
                "consecutive_nominal_checks": 142,
                "cooldown_time_remaining_s": self.cooldown_remaining
            },
            "cryptographic_attestation": {
                "sensor_log_hash": "sha256:5ef4919bc01a756616238b16e4db7c88b9015e3bf4f0d2b0b822cd15d6c15b0f",
                "tpm_signature": "eddsa:mock_tpm_signature_value"
            }
        }
        
        with open(TELEMETRY_PATH, "w") as f:
            json.dump(payload, f, indent=2)

def run_simulation():
    node = AltarNode()
    print("[SIMULATOR] Initializing mock Altar node telemetry daemon...")
    
    # 1. Run 2 nominal checks
    for _ in range(2):
        node.generate_metrics(spike=False)
        node.export_telemetry()
        print(f"[SIMULATOR] Status: {node.state} | Core Temp: {node.gpu_core:.1f}°C | Memory Junction: {node.gpu_vram:.1f}°C")
        time.sleep(1)

    # 2. Trigger critical thermal spike
    print("\n[SIMULATOR] Spiking GPU memory junction to force critical breach...")
    node.generate_metrics(spike=True)
    node.export_telemetry()
    
    # 3. Trigger transition to recovery
    if node.state == "SUSPENDED":
        node.state = "RECOVERY"
        print("\n[SIMULATOR] Transitioning to RECOVERY state. Executing cooling cycle...")
        for _ in range(3):
            node.generate_metrics(spike=False)
            node.export_telemetry()
            print(f"[SIMULATOR] Status: {node.state} | Memory Junction cooled to: {node.gpu_vram:.1f}°C")
            time.sleep(1)

if __name__ == "__main__":
    run_simulation()