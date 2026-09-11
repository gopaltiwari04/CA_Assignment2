#!/bin/bash

set -e

GEM5=~/gem5/build/X86/gem5.opt
CONFIG=~/CA_Assignment2/part2/configs/x86_se_config.py
BENCHDIR=~/CA_Assignment2/part2/benchmarks
RESULTDIR=~/CA_Assignment2/part2/results

BENCHMARKS=(
    int_arithmetic
    independent_int
    float_compute
    memory_access
    mixed_compute
)

for FU in 1 2 3 4; do
    for BENCH in "${BENCHMARKS[@]}"; do
        OUTDIR="$RESULTDIR/fu${FU}/${BENCH}"

        echo "========================================"
        echo "Running FU${FU} - ${BENCH}"
        echo "Output: ${OUTDIR}"
        echo "========================================"

        rm -rf "$OUTDIR"
        mkdir -p "$OUTDIR"

        "$GEM5" \
            -d "$OUTDIR" \
            "$CONFIG" \
            "$BENCHDIR/$BENCH" \
            --fu-config "$FU"

        echo "Completed FU${FU} - ${BENCH}"
        echo
    done
done

echo "========================================"
echo "All 20 simulations completed."
echo "========================================"