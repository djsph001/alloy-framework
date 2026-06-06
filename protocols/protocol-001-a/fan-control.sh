#!/usr/bin/env bash
# fan-control.sh — Ampere fan curve override for adversarial rounds.
#
# REQUIRES AN ACTIVE X SERVER. Will NOT work on headless servers.
# For the Z4G4 running headless, use coolercontrol or an NVML-direct tool
# instead. See protocol-001-a/README.md §001-A.2.2.

# Unlock manual fan control if cool-bits are enabled
sudo nvidia-xconfig --cool-bits=4

# Set a static 65% fan speed during adversarial rounds
nvidia-settings -a "[fan:0]/GPUTargetFanSpeed=65" -a "[fan:1]/GPUTargetFanSpeed=65"
