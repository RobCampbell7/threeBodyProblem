from body import Body
from math import atan2, sin, cos

G = 6.6743015 * 10**(-11)

def dist2(b1, b2):
    return (b1.xPos - b2.xPos)**2 + (b1.yPos - b2.yPos)**2

def calculateAcceleration(b1, b2):
    a = G * b2.mass / dist2(b1, b2)
    theta = atan2(b2.yPos - b1.yPos, b2.xPos - b1.xPos)
    return (a * cos(theta), a * sin(theta))

def tupleSum(t1, t2):
    return (t1[0] + t2[0], t1[1] + t2[1])

class Simulation:
    def __init__(self):
        self.bodies = []
        self.n = 0

    def addBody(self, mass = 1., pos=(0., 0.), vel=(0., 0.), acc=(0., 0.)):
        self.bodies.append(Body(
            mass = mass,
            pos = pos,
            vel = vel,
            acc = acc
        ))
        self.n += 1

    def iterate(self, t = 1):
        accelerations = [(0, 0) for i in range(self.n)]
        for i in range(self.n):
            for j in range(self.n):
                if i != j:
                    accelerations[i] = tupleSum(accelerations[i], calculateAcceleration(self.bodies[i], self.bodies[j]))
        for b in self.bodies:
            b.iterate(t, accelerations[i])