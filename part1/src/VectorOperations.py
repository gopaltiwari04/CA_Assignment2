from m5.SimObject import SimObject


class VectorOperations(SimObject):
    type = "VectorOperations"
    cxx_header = "vector_operations/vector_operations.hh"
    cxx_class = "gem5::VectorOperations"