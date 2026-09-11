# Assignment 2 - Part 2
## Functional Unit Configuration and Microbenchmark Evaluation

## 1. Objective

This part of the assignment evaluates the effect of different functional-unit latency and pipeline configurations on five microbenchmarks using gem5.

The experiments use an X86 out-of-order CPU in SE mode. Four functional-unit configurations are evaluated using the latency and pipeline properties specified in the assignment.

---

## 2. System Configuration

| Component | Configuration |
|---|---|
| ISA | X86 |
| Simulation Mode | System Emulation (SE) |
| CPU | Out-of-order (O3) |
| CPU Cores | 1 |
| CPU Frequency | 3 GHz |
| L1 Instruction Cache | 32 KiB, 4-way |
| L1 Data Cache | 32 KiB, 4-way |
| L2 Cache | 256 KiB, 8-way |
| L2 Organization | Shared |
| Memory | Single-channel DDR4-2400 |
| Memory Size | 3 GB |
| gem5 Version | 24.0.0.0 |

The cache hierarchy uses gem5's `PrivateL1SharedL2CacheHierarchy`, providing private L1 instruction/data caches and a shared L2 cache.

---

## 3. Functional Unit Configurations

The assignment specifies the functional-unit values as **(Latency, Pipeline)**.

| Operation | FU1 | FU2 | FU3 | FU4 |
|---|---|---|---|---|
| IntALU | (1, true) | (2, true) | (1, false) | (2, false) |
| IntDiv | (4, true) | (6, true) | (4, false) | (6, false) |
| FloatMul | (10, true) | (15, true) | (10, true) | (15, false) |
| MemRead | (2, true) | (4, true) | (2, false) | (4, false) |
| FloatMemWrite | (1, true) | (2, true) | (2, false) | (3, false) |

The default gem5 functional-unit counts are retained. Only the specified operation latency and pipeline properties are changed.

Other ISA-required operation classes are preserved so that the X86 processor can execute correctly.

The custom FU configurations are implemented in:

```text
configs/fu_configs.py
```

and selected by:

```text
configs/x86_se_config.py
```

using the `--fu-config` argument.

---

## 4. Microbenchmarks

Five microbenchmarks were implemented.

### 4.1 int_arithmetic

Performs repeated integer arithmetic operations, including modulo/division operations.

### 4.2 independent_int

Performs several independent integer additions to evaluate integer execution throughput.

### 4.3 float_compute

Performs repeated floating-point multiplication and addition operations.

### 4.4 memory_access

Initializes a large array outside the ROI and repeatedly accesses the array inside the ROI to evaluate memory behavior.

### 4.5 mixed_compute

Combines array accesses with floating-point multiplication and addition operations.

All five benchmark source files contain fewer than 25 lines as required.

---

## 5. ROI Measurement

Each benchmark uses:

```cpp
m5_work_begin(0, 0);
```

immediately before the measured computation and:

```cpp
m5_work_end(0, 0);
```

immediately after it.

Initialization and setup are outside the ROI where applicable. Therefore, the reported statistics represent the measured benchmark region rather than setup overhead.

The default gem5 behavior resets statistics at `m5_work_begin()` and dumps statistics at `m5_work_end()`.

---

## 6. Build Instructions

From the `part2` directory:

```bash
make
```

This builds all five benchmark binaries using the gem5 `m5ops` library.

---

## 7. Run Instructions

To run all 20 experiments (5 benchmarks × 4 FU configurations):

```bash
bash run_all.sh
```

An individual configuration can be run using:

```bash
~/gem5/build/X86/gem5.opt \
    --outdir=results/fu1/int_arithmetic \
    configs/x86_se_config.py \
    benchmarks/int_arithmetic \
    --fu-config 1
```

The FU configuration can be selected with values `1`, `2`, `3`, or `4`.

Results are stored under:

```text
results/fu1/
results/fu2/
results/fu3/
results/fu4/
```

---

## 8. Results

The following table reports the ROI statistics for all 20 experiments.

| FU | Benchmark | SimTicks | Cycles | CPI | IPC |
|---:|---|---:|---:|---:|---:|
| 1 | int_arithmetic | 17,316,363,303 | 52,001,091 | 1.019629 | 0.980749 |
| 1 | independent_int | 3,493,620,549 | 10,491,353 | 0.749382 | 1.334433 |
| 1 | float_compute | 3,330,278,721 | 10,000,837 | 0.555602 | 1.799851 |
| 1 | memory_access | 9,301,302,387 | 27,931,839 | 0.761080 | 1.313922 |
| 1 | mixed_compute | 1,659,888,783 | 4,984,651 | 0.845096 | 1.183298 |
| 2 | int_arithmetic | 25,308,381,285 | 76,001,145 | 1.490218 | 0.671043 |
| 2 | independent_int | 5,328,195,138 | 16,000,586 | 1.142898 | 0.874968 |
| 2 | float_compute | 3,996,236,763 | 12,000,711 | 0.666706 | 1.499912 |
| 2 | memory_access | 14,350,486,149 | 43,094,553 | 1.174231 | 0.851621 |
| 2 | mixed_compute | 1,761,444,126 | 5,289,622 | 0.896800 | 1.115076 |
| 3 | int_arithmetic | 17,316,363,969 | 52,001,093 | 1.019629 | 0.980749 |
| 3 | independent_int | 3,493,624,878 | 10,491,366 | 0.749383 | 1.334431 |
| 3 | float_compute | 3,996,239,760 | 12,000,720 | 0.666706 | 1.499911 |
| 3 | memory_access | 9,301,862,493 | 27,933,521 | 0.761126 | 1.313842 |
| 3 | mixed_compute | 1,763,127,774 | 5,294,678 | 0.897657 | 1.114011 |
| 4 | int_arithmetic | 25,308,381,618 | 76,001,146 | 1.490218 | 0.671043 |
| 4 | independent_int | 5,328,213,120 | 16,000,640 | 1.142902 | 0.874966 |
| 4 | float_compute | 4,677,503,148 | 14,046,556 | 0.780364 | 1.281454 |
| 4 | memory_access | 14,352,216,084 | 43,099,748 | 1.174372 | 0.851519 |
| 4 | mixed_compute | 1,826,182,656 | 5,484,032 | 0.929760 | 1.075546 |

---

## 9. Performance Analysis

### 9.1 Overall Observation

FU1 gives the lowest simulation time for all five benchmarks and therefore provides the best overall performance among the four configurations.

### 9.2 FU1 vs FU2

FU2 increases the latency of the specified operation classes while keeping them pipelined.

Relative to FU1, FU2 is approximately:

| Benchmark | FU2 slowdown |
|---|---:|
| int_arithmetic | 46.16% |
| independent_int | 52.49% |
| float_compute | 20.00% |
| memory_access | 54.29% |
| mixed_compute | 6.12% |

The largest slowdowns occur for `memory_access` and `independent_int`, while `mixed_compute` is affected the least.

### 9.3 FU1 vs FU3

FU3 retains the same latency as FU1 for IntALU, IntDiv, FloatMul and MemRead, but makes several operations non-pipelined.

The integer-heavy benchmarks are almost unchanged:

- `int_arithmetic`: approximately unchanged
- `independent_int`: approximately unchanged
- `memory_access`: approximately unchanged

However, `float_compute` is approximately 20% slower and `mixed_compute` is approximately 6.22% slower.

This shows that removing pipelining can affect O3 CPU performance even when operation latency remains unchanged.

### 9.4 FU2 vs FU4

FU4 combines the higher latencies of FU2 with additional non-pipelined operations.

The integer and memory benchmarks are nearly unchanged compared with FU2, while:

- `float_compute` is approximately 17% slower
- `mixed_compute` is approximately 3.67% slower

The largest degradation is observed for floating-point computation.

### 9.5 Benchmark-Specific Observations

**int_arithmetic:**  
Strongly affected by integer functional-unit latency. FU1 is significantly faster than FU2 and FU4.

**independent_int:**  
Benefits from low integer latency and pipelining. FU1 has the highest IPC.

**float_compute:**  
Particularly sensitive to floating-point functional-unit latency and pipelining. FU4 is the slowest configuration.

**memory_access:**  
Affected by memory operation latency and its interaction with the CPU pipeline.

**mixed_compute:**  
The least sensitive benchmark overall, with comparatively smaller differences between configurations.

---

## 10. Statistics Snippets

Example FU1 ROI statistics are provided in:

```text
results/examples/
```

The files are:

```text
results/examples/int_arithmetic_stats.txt
results/examples/independent_int_stats.txt
results/examples/float_compute_stats.txt
results/examples/memory_access_stats.txt
results/examples/mixed_compute_stats.txt
```

Example:

```text
===== int_arithmetic : FU1 ROI statistics =====
simSeconds                                   0.017316
simTicks                                  17316363303
simInsts                                     51626401
simOps                                       75167474
board.processor.cores.core.numCycles         52001091
board.processor.cores.core.cpi               1.019629
board.processor.cores.core.ipc               0.980749
```

---

## 11. Tricky Requirements / Design Decisions

### Functional-unit interpretation

The assignment table specifies **(Latency, Pipeline)** values rather than functional-unit counts. Therefore, the default gem5 FU counts were retained.

### ISA-required operations

The X86 ISA requires additional operation classes beyond those explicitly listed in the assignment. These operation classes were preserved so that the processor could execute correctly.

### Memory operations

The scalar `MemRead` and `FloatMemWrite` operation properties were modified in the custom read/write functional-unit description.

### ROI

Initialization is outside the ROI where applicable. Only the benchmark computation is placed between `m5_work_begin()` and `m5_work_end()`.

### Benchmark size

All five benchmark source files contain fewer than 25 lines.

### DRAM warning

gem5 reports the following warning:

```text
DRAM device capacity (16384 Mbytes) does not match the address range assigned (4096 Mbytes)
```

This is a gem5 model warning. The simulations completed successfully and produced valid statistics.

---

## 12. Files Included

```text
part2/
├── Makefile
├── README.md
├── run_all.sh
├── extract_results.py
│
├── configs/
│   ├── fu_configs.py
│   └── x86_se_config.py
│
├── benchmarks/
│   ├── int_arithmetic.cpp
│   ├── independent_int.cpp
│   ├── float_compute.cpp
│   ├── memory_access.cpp
│   └── mixed_compute.cpp
│
└── results/
    ├── results.csv
    └── examples/
        ├── int_arithmetic_stats.txt
        ├── independent_int_stats.txt
        ├── float_compute_stats.txt
        ├── memory_access_stats.txt
        └── mixed_compute_stats.txt
```

---

## 13. Conclusion

The experiments demonstrate that functional-unit latency and pipelining have a measurable effect on O3 CPU performance.

Among the four configurations, FU1 consistently provides the best performance across all five microbenchmarks. FU2's increased latencies cause significant slowdowns, while the non-pipelined operations in FU3 and FU4 further affect workloads with relevant execution dependencies and resource use.

All five microbenchmarks were successfully evaluated under all four functional-unit configurations.