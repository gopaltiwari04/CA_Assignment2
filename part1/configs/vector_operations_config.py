import m5
from m5.objects import Root, VectorOperations


vector_operations = VectorOperations()

root = Root(full_system=False)
root.vector_operations = vector_operations

m5.instantiate()

print("Starting VectorOperations simulation...")

exit_event = m5.simulate(15000)

print(
    f"Simulation finished at tick {m5.curTick()} "
    f"because {exit_event.getCause()}"
)
