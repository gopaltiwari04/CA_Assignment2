import csv
import re
from pathlib import Path

BASE = Path(__file__).resolve().parent
RESULTS = BASE / "results"

BENCHMARKS = [
    "int_arithmetic",
    "independent_int",
    "float_compute",
    "memory_access",
    "mixed_compute",
]


def get_stat(stats_text, name):
    pattern = rf"^{re.escape(name)}\s+([-+0-9.eE]+)"
    match = re.search(pattern, stats_text, re.MULTILINE)
    return float(match.group(1)) if match else None


def get_roi_stats(path):
    text = path.read_text()

    blocks = re.findall(
        r"-{10} Begin Simulation Statistics -{10}(.*?)-{10} End Simulation Statistics\s+-{10}",
        text,
        re.DOTALL,
    )

    if not blocks:
        raise RuntimeError(f"No statistics block found in {path}")

    # The first block is the ROI dumped by m5_work_end().
    roi = blocks[0]

    return {
        "simTicks": get_stat(roi, "simTicks"),
        "simInsts": get_stat(roi, "simInsts"),
        "simOps": get_stat(roi, "simOps"),
        "numCycles": get_stat(
            roi, "board.processor.cores.core.numCycles"
        ),
        "cpi": get_stat(
            roi, "board.processor.cores.core.cpi"
        ),
        "ipc": get_stat(
            roi, "board.processor.cores.core.ipc"
        ),
        "l1d_accesses": get_stat(
            roi,
            "board.cache_hierarchy.l1dcaches.demandAccesses::total",
        ),
        "l1d_hits": get_stat(
            roi,
            "board.cache_hierarchy.l1dcaches.demandHits::total",
        ),
        "l1i_accesses": get_stat(
            roi,
            "board.cache_hierarchy.l1icaches.demandAccesses::total",
        ),
        "l1i_hits": get_stat(
            roi,
            "board.cache_hierarchy.l1icaches.demandHits::total",
        ),
        "l1i_misses": get_stat(
            roi,
            "board.cache_hierarchy.l1icaches.demandMisses::total",
        ),
        "l2_accesses": get_stat(
            roi,
            "board.cache_hierarchy.l2cache.demandAccesses::total",
        ),
        "l2_misses": get_stat(
            roi,
            "board.cache_hierarchy.l2cache.demandMisses::total",
        ),
    }


rows = []

for fu in range(1, 5):
    for benchmark in BENCHMARKS:
        stats_path = RESULTS / f"fu{fu}" / benchmark / "stats.txt"

        if not stats_path.exists():
            print(f"WARNING: missing {stats_path}")
            continue

        stats = get_roi_stats(stats_path)

        row = {
            "FU": fu,
            "Benchmark": benchmark,
            **stats,
        }

        rows.append(row)

output = RESULTS / "results.csv"

fieldnames = [
    "FU",
    "Benchmark",
    "simTicks",
    "simInsts",
    "simOps",
    "numCycles",
    "cpi",
    "ipc",
    "l1d_accesses",
    "l1d_hits",
    "l1i_accesses",
    "l1i_hits",
    "l1i_misses",
    "l2_accesses",
    "l2_misses",
]

with output.open("w", newline="") as f:
    writer = csv.DictWriter(f, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(rows)

print(f"Extracted {len(rows)} simulation results.")
print(f"Saved to: {output}")