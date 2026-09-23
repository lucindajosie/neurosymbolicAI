from z3 import *

x = Int("x")

solver = Solver()

solver.add(x > 0, x < 10)

if solver.check() == sat:
    model = solver.model()
    print(model.evaluate(x))