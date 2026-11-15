class Body:
    def __init__(self, mass:float, pos, vel, acc):
        # self.xPos, self.yPos = 0, 0
        # self.xVel, self.yVel = 0, 0
        # self.xAcc, self.yAcc = 0, 0
        self.mass = mass
        self.xPos, self.yPos = pos
        self.xVel, self.yVel = vel
        self.xAcc, self.yAcc = acc

    def iterate(self, t=1, newAcc=None):
        # step forward by t using the average of the old and new acceleration,
        # a rough velocity verlet so the step isn't biased to either end
        if newAcc != None:
            xAcc = (self.xAcc + newAcc[0]) / 2
            yAcc = (self.yAcc + newAcc[1]) / 2
        else:
            xAcc = self.xAcc
            yAcc = self.yAcc
            
        # s = ut + at^2/2, then v = u + at
        self.xPos += self.xVel * t + 0.5 * xAcc * t**2
        self.yPos += self.yVel * t + 0.5 * yAcc * t**2
        self.xVel += xAcc * t
        self.yVel += yAcc * t
        if newAcc != None:
            # keep the new acceleration so it can be averaged with the next one
            self.xAcc, self.yAcc = newAcc