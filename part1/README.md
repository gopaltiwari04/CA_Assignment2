# Part 1 - Vector Operations SimObject

## Overview

This part implements a custom gem5 SimObject named `VectorOperations`.

The SimObject performs three vector operations using scheduled gem5 events:

1. Vector Dot Product
2. Vector Compare
3. Vector Multiply-Accumulate (MAC)

The three operations are scheduled at different simulation ticks.

---

## Input Vectors

The following vectors are hardcoded in the SimObject:

A = [1, 2, 3, 4, 5]

B = [5, 4, 3, 2, 1]

C = [10, 10, 10, 10, 10]

---

## Events

The SimObject contains three events:

| Event | Simulation Tick | Operation |
|---|---:|---|
| VectorDotProduct | 150 | Computes the dot product of A and B |
| VectorCompare | 1500 | Compares A and B element by element |
| VectorMAC | 15000 | Computes A[i] × B[i] + C[i] |

---

## Vector Dot Product

The dot product is calculated as:

A · B = Σ A[i] × B[i]

For the given vectors:

1×5 + 2×4 + 3×3 + 4×2 + 5×1 = 35

Therefore:

Dot Product = 35

---

## Vector Compare

Each element of A is compared with the corresponding element of B.

A = [1, 2, 3, 4, 5]

B = [5, 4, 3, 2, 1]

The resulting comparison vector is:

[0, 0, 1, 0, 0]

Here, `1` represents equal elements and `0` represents unequal elements.

---

## Vector MAC

The MAC operation computes:

C[i] = A[i] × B[i] + C[i]

For the given vectors:

[1×5+10, 2×4+10, 3×3+10, 4×2+10, 5×1+10]

The resulting vector is:

[15, 18, 19, 18, 15]

---

## Debug Flags

The following gem5 debug flags are implemented:

| Debug Flag | Description |
|---|---|
| VECTOR | Displays the input vectors |
| RESULTDOT | Displays the dot product result |
| COMPARE | Displays the vector comparison result |
| RESULTMAC | Displays the MAC result |

The flags can be enabled using:

```bash
--debug-flags=VECTOR,RESULTDOT,COMPARE,RESULTMAC
