import argparse

from fu_configs import FUConfig1, FUConfig2, FUConfig3, FUConfig4
from gem5.components.boards.x86_board import X86Board
from gem5.components.boards.se_binary_workload import SEBinaryWorkload
from gem5.components.cachehierarchies.classic.private_l1_shared_l2_cache_hierarchy import (
    PrivateL1SharedL2CacheHierarchy,
)
from gem5.components.memory import SingleChannelDDR4_2400
from gem5.components.processors.cpu_types import CPUTypes
from gem5.components.processors.simple_processor import SimpleProcessor
from gem5.isas import ISA
from gem5.resources.resource import BinaryResource
from gem5.simulate.simulator import Simulator


class X86SEBoard(X86Board, SEBinaryWorkload):
    pass


parser = argparse.ArgumentParser()
parser.add_argument("binary")
parser.add_argument("--fu-config", type=int, choices=[1, 2, 3, 4], default=1)
args = parser.parse_args()


processor = SimpleProcessor(
    cpu_type=CPUTypes.O3,
    num_cores=1,
    isa=ISA.X86,
)

fu_configs = {
    1: FUConfig1,
    2: FUConfig2,
    3: FUConfig3,
    4: FUConfig4,
}

processor.get_cores()[0].core.fuPool = fu_configs[args.fu_config]()

cache_hierarchy = PrivateL1SharedL2CacheHierarchy(
    l1d_size="32KiB",
    l1i_size="32KiB",
    l2_size="256KiB",
    l1d_assoc=4,
    l1i_assoc=4,
    l2_assoc=8,
)

memory = SingleChannelDDR4_2400(size="3GB")

board = X86SEBoard(
    clk_freq="3GHz",
    processor=processor,
    memory=memory,
    cache_hierarchy=cache_hierarchy,
)

board.set_se_binary_workload(
    BinaryResource(args.binary)
)

simulator = Simulator(board=board)
simulator.run()