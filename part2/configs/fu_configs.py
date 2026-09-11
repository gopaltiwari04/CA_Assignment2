from m5.objects import FUPool, FUDesc, OpDesc
from m5.objects.FuncUnitConfig import (
    FP_ALU,
    SIMD_Unit,
    PredALU,
    IprPort,
)


def make_desc(name, count, operations):
    return type(
        name,
        (FUDesc,),
        {
            "count": count,
            "opList": [
                OpDesc(
                    opClass=op_class,
                    opLat=latency,
                    pipelined=pipeline,
                )
                for op_class, latency, pipeline in operations
            ],
        },
    )()


def make_pool(
    name,
    int_alu,
    int_div,
    float_mul,
    mem_read,
    float_mem_write,
):
    return type(
        name,
        (FUPool,),
        {
            "FUList": [
                # Keep the normal number of integer ALUs.
                make_desc(
                    name + "IntALU",
                    6,
                    [
                        ("IntAlu", int_alu[0], int_alu[1]),
                    ],
                ),

                # Keep IntMult available for normal X86 execution.
                # Only IntDiv is controlled by the assignment.
                make_desc(
                    name + "IntMultDiv",
                    2,
                    [
                        ("IntMult", 3, True),
                        ("IntDiv", int_div[0], int_div[1]),
                    ],
                ),

                # Keep normal floating-point ALU operations.
                FP_ALU(),

                # FloatMult is controlled by the assignment.
                # Other normal FP operations remain available.
                make_desc(
                    name + "FPMultDiv",
                    2,
                    [
                        ("FloatMult", float_mul[0], float_mul[1]),
                        ("FloatMultAcc", 5, True),
                        ("FloatMisc", 3, True),
                        ("FloatDiv", 12, False),
                        ("FloatSqrt", 24, False),
                    ],
                ),

                # Keep SIMD operations available.
                SIMD_Unit(),
                PredALU(),

                # Normal memory operations.
                # The assignment-controlled MemRead and
                # FloatMemWrite properties are changed here.
                make_desc(
                    name + "RdWrPort",
                    4,
                    [
                        ("MemRead", mem_read[0], mem_read[1]),
                        ("MemWrite", 1, True),
                        ("FloatMemRead", 1, True),
                        (
                            "FloatMemWrite",
                            float_mem_write[0],
                            float_mem_write[1],
                        ),

                        # Supported SIMD memory operations in
                        # gem5 24.0.0.0.
                        ("SimdUnitStrideLoad", 1, True),
                        ("SimdUnitStrideStore", 1, True),
                        ("SimdUnitStrideMaskLoad", 1, True),
                        ("SimdUnitStrideMaskStore", 1, True),
                        ("SimdUnitStrideSegmentedLoad", 1, True),
                        ("SimdUnitStrideSegmentedStore", 1, True),
                        ("SimdStridedLoad", 1, True),
                        ("SimdStridedStore", 1, True),
                        ("SimdIndexedLoad", 1, True),
                        ("SimdIndexedStore", 1, True),
                        ("SimdUnitStrideFaultOnlyFirstLoad", 1, True),
                        ("SimdWholeRegisterLoad", 1, True),
                        ("SimdWholeRegisterStore", 1, True),
                    ],
                ),

                IprPort(),
            ],
        },
    )


class FUConfig1(
    make_pool(
        "FUConfig1",
        (1, True),
        (4, True),
        (10, True),
        (2, True),
        (1, True),
    )
):
    pass


class FUConfig2(
    make_pool(
        "FUConfig2",
        (2, True),
        (6, True),
        (15, True),
        (4, True),
        (2, True),
    )
):
    pass


class FUConfig3(
    make_pool(
        "FUConfig3",
        (1, False),
        (4, False),
        (10, True),
        (2, False),
        (2, False),
    )
):
    pass


class FUConfig4(
    make_pool(
        "FUConfig4",
        (2, False),
        (6, False),
        (15, False),
        (4, False),
        (3, False),
    )
):
    pass