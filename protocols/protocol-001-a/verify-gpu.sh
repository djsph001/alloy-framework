#!/usr/bin/env bash
# Verify the container can see both GPUs.
# Run after `docker compose up -d` to confirm Tensor-core path is live.

docker run --rm --gpus all mycelial-query nvidia-smi
