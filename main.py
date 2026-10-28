from copy import deepcopy
import matplotlib.pyplot as plt
import matplotlib as mpl
from matplotlib.animation import FuncAnimation, FFMpegWriter
from simulation import Simulation

minDist = 1000
def dist(p1, p2):
    return (p1[0] - p2[0]) ** 2 + (p1[1] - p2[1])

mpl.rcParams['animation.ffmpeg_path'] = r'C:\\Users\\rhc209\\OneDrive - University of Exeter\\python\\ffmpeg-master-latest-win64-gpl\\bin\\ffmpeg.exe'
k = -1
def update(frame):
    # global minDist
    if frame > 0:
        sim.iterate(t=1)

    pos = sim.positions()
    # minDist = min(minDist, dist(pos[0], pos[1]))
    # print(dist(pos[0], pos[1]))
    # print(*pos, sep=", ")
    # print(*[(b.xAcc, b.yAcc) for b in sim.bodies], sep=", ")
    # print(*[(b.xVel, b.yVel) for b in sim.bodies], sep=", ")
    # print()
    for i in range(sim.n):
        points[i].set_data(*pos[i])

    return *points,

sim = Simulation()
sim.addBody(1, (0, 0.5), (0.001, 0.001))
sim.addBody(1, (0.5, 0.3), (-0.001, -0.0005))
sim.addBody(1, (0, -0.2), (0.001, 0.0005))
# sim.addBody(10000, (0, 0))
# sim.addBody(10, (0, 0))

fig, ax = plt.subplots(figsize=(5, 5))
ax.grid(which="major")
ax.grid(which="minor", linestyle="--")
ax.set_xlim(-1, 1)
ax.set_ylim(-1, 1)
points = []
arrows = []
colours = ["r", "g", "b", "k"]
for i in range(sim.n):
    # newPlot, = fig.plot(*p, "rx")
    points.append(ax.plot(sim.bodies[i].xPos, sim.bodies[i].yPos, colours[i] + ".")[0])

ani = FuncAnimation(fig, update, frames=100000, interval=0, blit=True, repeat=False)#, init_func=init)
plt.show()
