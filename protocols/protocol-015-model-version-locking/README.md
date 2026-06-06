---
title: "Protocol 015: Model Version Locking"
category: "Epistemic Infrastructure"
status: "Active"
version: "1.0"
systemic_anchor: "The Emergence Collective / The Digital Lakou"
depends_on: ["Protocol 014 (Adversarial Synthesis)"]
referenced_by: ["Protocol 016 (Hallucination Remediation)", "Version Compatibility Matrix"]
tags: ["Version Pinning", "API Hardening", "Drift Detection", "Calibration"]
lead_synthesis: "Dale Joseph"
contributors: ["Claude (Anthropic)", "Grok (xAI)", "Gemini (Google DeepMind)", "ChatGPT (OpenAI)", "DeepSeek"]
---

# Protocol 015: Model Version Locking

**Layer:** Epistemic Infrastructure
**Systemic Anchor:** The Emergence Collective / The Digital Lakou
**Status:** Active
**Lead Synthesis:** Dale Joseph, with Claude, Grok, Gemini, ChatGPT, and DeepSeek

---

## Executive Summary

The integrity of **Protocol 014: Adversarial Synthesis** relies on a stable baseline of model behaviors. Because frontier AI developers deploy silent weight updates, RLHF adjustments, and system prompt shifts over commercial APIs, a model's capacity for defection, alignment faking, and reasoning is subject to silent drift. This drift alters the communication friction coefficient (gamma) and degrades the reliability of the Forge without throwing runtime errors.

**Protocol 015** establishes the compliance standards for freezing, validating, and documenting the precise model dependencies required to run the Epistemic Layer.

---

## 1. The Model Manifest and API Pinning

Under no circumstances are wildcard or "latest" API endpoints (e.g., claude-3-5-sonnet-latest or gpt-4o) permitted within the active research pipeline. Every connection to Tier 2 and Tier 3 models must target a specific, immutable version snapshot.

### 1.1 The Active Manifest (Mid-2026 Benchmark)

```yaml
manifest_version: "1.1.0"
frozen_on: "2026-06-05"
compatibility_hash: "sha256:d8a9c394ef0015a3bf4f1b2b0b822cd15d6c15b0f00a0822e039485"

models:
  tier_2_frontier:
    claude:
      endpoint: "claude-3-5-sonnet-20241022"
      temperature: 0.1
      max_tokens: 4096
    grok:
      endpoint: "grok-2-20250115"
      temperature: 0.2
      max_tokens: 4096

  tier_3_general:
    gemini:
      endpoint: "gemini-1.5-pro-002"
      temperature: 0.0
      max_tokens: 8192
    chatgpt:
      endpoint: "gpt-4o-2024-08-06"
      temperature: 0.0
      max_tokens: 4096
    deepseek:
      endpoint: "deepseek-chat"  # Pin to frozen API revision header: "v2026-02-01"
      temperature: 0.1
      max_tokens: 8192
```

---

## 2. Parameter Hardening

To guarantee that the **Adversarial Prompt Set (Assets A and B)** produces repeatable, forensic-grade outputs, all API wrappers must enforce strict, deterministic parameter bounds.

1. **Deterministic Temperature:** General Models (Tier 3) used for fact-checking and cross-examination *must* enforce a temperature of **0.0** to eliminate stochastic variation in factual verification.

2. **Strategic Temperature:** Frontier Models (Tier 2) used for adversarial sparring must enforce a temperature between **0.1** and **0.2**. This range provides sufficient cognitive breadth to locate arguments' hidden "blind spots" without slipping into unverifiable speculation.

3. **System Prompt Precedence:** Local API integrations must override any default developer system instructions with the explicit, unmodified text of Asset A or Asset B.

---

## 3. Drift Detection and Invalidation

Even with explicit version pinning, cloud host providers occasionally apply behind-the-scenes patching or safety filter adjustments. The Human Conductor must monitor the system for "silent drift."

### 3.1 The Drift Metrics

Every five (5) sessions, the Conductor must compare current run logs against the baseline **Carrington Scorecard** data, calculating the variance in communication friction:

> delta_gamma = |gamma_current - gamma_baseline|

### 3.2 Invalidation Rules

- **Rule A (Friction Variance):** If delta_gamma >= 0.15 over three consecutive sessions without a change in the human conductor or core thesis complexity, the model manifest is flagged as **Compromised by Silent Drift**.

- **Rule B (Defection Failure):** If a Tier 2 model fails to register a defection during the monthly spot-check (using a mini-Carrington trap), the manifest is invalidated.

- **Consequence:** Upon invalidation, the entire system must halt live research operations until a full **Carrington Calibration Run** is completed, evaluated, and signed off by the Independent Auditor.
