from body import Body
from math import sin, cos, pi

G = 6.6743015 * 10**(-11)

def dist2(b1, b2):
    return (b1.xPos - b2.xPos)**2 + (b1.yPos - b2.yPos)**2

def calculateAcceleration(b1, b2):
    return G * b1.mass * b2.mass / dist2(b1, b2)

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
