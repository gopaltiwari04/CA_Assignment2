# Part 1 - Vector Operations SimObject

## Overview

This part implements a custom gem5 SimObject named `VectorOperations`.

The SimObject performs three vector operations using scheduled gem5 events:

1. Vector Dot Product
2. Vector Compare
3. Vector Multiply-Accumulate (MAC)

The three operations are scheduled at simulation ticks 150, 1500, and 15000 respectively.

---

## Input Vectors

The following vectors are hardcoded in the SimObject:

```text
A = [1, 2, 3, 4, 5]
B = [5, 4, 3, 2, 1]
C = [10, 10, 10, 10, 10]
```

No user input is required.

---

## Events

The SimObject contains three scheduled events:

| Event | Simulation Tick | Operation |
|---|---:|---|
| VectorDotProduct | 150 | Computes the dot product of A and B |
| VectorCompare | 1500 | Compares A and B element by element |
| VectorMAC | 15000 | Computes A[i] × B[i] + C[i] |

---

## Vector Dot Product

The dot product is calculated as:

```text
A · B = Σ A[i] × B[i]
```

For the given vectors:

```text
1×5 + 2×4 + 3×3 + 4×2 + 5×1 = 35
```

Therefore:

```text
Dot Product = 35
```

---

## Vector Compare

Each element of A is compared with the corresponding element of B.

```text
A = [1, 2, 3, 4, 5]
B = [5, 4, 3, 2, 1]
```

The resulting comparison vector is:

```text
[0, 0, 1, 0, 0]
```

Here, `1` represents equal elements and `0` represents unequal elements.

---

## Vector MAC

The MAC operation computes:

```text
C[i] = A[i] × B[i] + C[i]
```

For the given vectors:

```text
[1×5+10, 2×4+10, 3×3+10, 4×2+10, 5×1+10]
```

The resulting vector is:

```text
[15, 18, 19, 18, 15]
```

---

## Source Files and Their Purpose

The implementation consists of the following files:

| File | Purpose |
|---|---|
| `vector_operations.hh` | Declares the `VectorOperations` SimObject class, vectors, events, and methods |
| `vector_operations.cc` | Implements the vector operations and scheduled event callbacks |
| `VectorOperations.py` | Defines the gem5 SimObject parameters and SimObject type |
| `SConscript` | Adds the C++ source files to the gem5 build system |
| Configuration script | Creates and instantiates the `VectorOperations` SimObject for simulation |

The SimObject source files are located under:

```text
gem5/src/vector_operations/
```

---

## Debug Flags

The following gem5 debug flags are implemented:

| Debug Flag | Description |
|---|---|
| `VECTOR` | Displays the input vectors |
| `RESULTDOT` | Displays the dot product result |
| `COMPARE` | Displays the vector comparison result |
| `RESULTMAC` | Displays the MAC result |

The flags can be enabled using:

```bash
--debug-flags=VECTOR,RESULTDOT,COMPARE,RESULTMAC
```

Each debug flag has a corresponding description/annotation so that its purpose is displayed by gem5.

---

## Build Instructions

From the gem5 directory:

```bash
cd ~/gem5
scons build/X86/gem5.opt -j$(nproc)
```

This builds gem5 with the custom `VectorOperations` SimObject.

---

## Run Instructions

Run the Part 1 configuration script using:

```bash
~/gem5/build/X86/gem5.opt configs/vector_operations_config.py
```

To enable all four debug flags:

```bash
~/gem5/build/X86/gem5.opt \
    --debug-flags=VECTOR,RESULTDOT,COMPARE,RESULTMAC \
    configs/vector_operations_config.py
```

The configuration script creates the `VectorOperations` SimObject and starts the simulation.

---

## Expected Results

The three events execute at their specified simulation ticks.

Expected results are:

```text
Vector Dot Product:
35

Vector Compare:
0 0 1 0 0

Vector MAC:
15 18 19 18 15
```

The final event executes at simulation tick 15000.

---

## Event Timing

| Event | Tick |
|---|---:|
| VectorDotProduct | 150 |
| VectorCompare | 1500 |
| VectorMAC | 15000 |

The events are scheduled using gem5's event scheduling mechanism. The resultant values are computed when the corresponding events are executed rather than being stored as precomputed results.

---

## Conclusion

The custom `VectorOperations` SimObject successfully implements the required VectorDotProduct, VectorCompare, and VectorMAC operations and schedules them at the required simulation ticks.

The required `VECTOR`, `RESULTDOT`, `COMPARE`, and `RESULTMAC` debug flags are also implemented to display the vectors and operation results during simulation.
