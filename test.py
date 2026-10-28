from copy import deepcopy
import matplotlib.pyplot as plt
from simulation import Simulation, calculateAcceleration

sim = Simulation()
sim.addBody(1, (-1, 0))
sim.addBody(1, (1, 0))

oldpositions = sim.positions()
for i in range(8):
    sim.iterate()

fig, ax = plt.subplots(figsize=(4, 4))
for p in sim.positions():
    ax.plot(*p, "r.")

for p in oldpositions:
    ax.plot(*p, "b.")
plt.ylim(-1, 1)
plt.grid()
plt.show()