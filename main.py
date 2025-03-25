from copy import deepcopy
import matplotlib.pyplot as plt
import matplotlib as mpl
from matplotlib.animation import FuncAnimation, FFMpegWriter
from simulation import Simulation

mpl.rcParams['animation.ffmpeg_path'] = r'C:\\Users\\rhc209\\OneDrive - University of Exeter\\python\\ffmpeg-master-latest-win64-gpl\\bin\\ffmpeg.exe'
k = -1
def update(frame):
    if frame > 0:
        sim.iterate()

    pos = sim.positions()
    print(*pos, sep=", ")
    for i in range(sim.n):
        plots[i].set_data(*pos[i])
    # print(*data, sep = ",\n")
    # plot2.set_data([x for x, y in swarm.particlePositions()],
    #                [y for x, y in swarm.particlePositions()])
    return *plots,

sim = Simulation()
sim.addBody(1, (-1, 0))
sim.addBody(1, (1, 0))

fig, ax = plt.subplots(figsize=(4, 4))
ax.grid()
ax.set_xlim(-5, 5)
ax.set_ylim(-5, 5)
plots = []
for p in sim.positions():
    # newPlot, = fig.plot(*p, "rx")
    plots.append(ax.plot(*p, "r.")[0])

ani = FuncAnimation(fig, update, frames=1000, interval=25, blit=True, repeat=False)#, init_func=init)
plt.show()
