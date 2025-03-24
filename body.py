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
        if newAcc != None:
            xAcc = (self.xAcc + newAcc[0]) / 2
            yAcc = (self.yAcc + newAcc[0]) / 2
        else:
            xAcc = self.xAcc
            yAcc = self.yAcc
            
        self.xPos += self.xVel * t + 0.5 * xAcc * t**2
        self.yPos += self.yVel * t + 0.5 * yAcc * t**2
        self.xVel += xAcc * t
        self.yVel += yAcc * t
        self.xAcc, self.yAcc = newAcc