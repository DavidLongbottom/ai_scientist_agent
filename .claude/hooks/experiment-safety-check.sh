#!/bin/bash
# Pre-experiment safety checks

if command -v nvidia-smi &> /dev/null; then
    # Quick GPU usage check
    USEDMEM=$(nvidia-smi --query-gpu=memory.used --format=csv,noheader,nounits | awk '{sum+=$1} END {print sum}')
    echo "[Safety Check] GPU Memory Used roughly: ${USEDMEM} MB"
else
    echo "[Safety Check] No nvidia-smi found. Proceeding with CPU/other device..."
fi

echo "[Safety Check] Validating API environments..."
if [ -z "$OPENAI_API_KEY" ] && [ -z "$ANTHROPIC_API_KEY" ]; then
    echo "ERROR: Neither OPENAI_API_KEY nor ANTHROPIC_API_KEY is found."
    echo "Failing safety check to prevent useless API calls."
    exit 1
fi

# Time limit checking logic ideally is enforced by wrapper, this script just prints a warning.
echo "[Safety Check] Remember to respect 3600s limits per step."
exit 0
