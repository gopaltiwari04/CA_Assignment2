# Assignment 2 - Part 2
## Functional Unit Configuration and Microbenchmark Evaluation

1. Objective

2. System Configuration
   - X86
   - SE mode
   - O3 CPU
   - 1 core
   - 3 GHz
   - Private L1 I/D
   - Shared L2
   - DDR4-2400
   - 3 GB

3. Functional Unit Configurations
   - FU1 table
   - FU2 table
   - FU3 table
   - FU4 table

4. Interpretation of FU Table
   - Values are (Latency, Pipeline)
   - Default gem5 FU counts retained
   - Only specified operation properties changed
   - Other ISA-required operations preserved

5. Microbenchmarks
   - int_arithmetic
   - independent_int
   - float_compute
   - memory_access
   - mixed_compute

6. ROI Measurement
   - m5_work_begin()
   - m5_work_end()
   - setup outside ROI

7. Build Instructions

8. Run Instructions

9. Results
   - complete results table

10. Analysis
    - FU1 vs FU2
    - FU1 vs FU3
    - FU2 vs FU4
    - benchmark-specific observations

11. Statistics Snippets
    - one snippet for each benchmark

12. Tricky Requirements / Design Decisions

13. Files Included