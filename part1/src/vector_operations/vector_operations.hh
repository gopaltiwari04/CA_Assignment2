#ifndef __VECTOR_OPERATIONS_HH__
#define __VECTOR_OPERATIONS_HH__

#include "sim/sim_object.hh"

namespace gem5
{

class VectorOperations : public SimObject
{
  public:
    VectorOperations(const VectorOperationsParams &p);

  private:
    void vectorDotProduct();
    void vectorCompare();
    void vectorMAC();
};

} // namespace gem5

#endif // __VECTOR_OPERATIONS_HH__