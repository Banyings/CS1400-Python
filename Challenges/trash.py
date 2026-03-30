import math

#class object
class Point:
    def __init__(self, initX, initY):
        self.x = initX
        self.y = initY

    def setX(self, incomingX):
        self.x = incomingX

    def setY(self, incomingY):
        self.y = incomingY

    def distanceTo(self, distanceX, distanceY):
        distance = math.sqrt(math.pow(self.y - distanceY, 2) + math.pow(self.x - distanceX, 2))
        return distance

    def __str__ (self):
        return 'Points: ',  self.x, ' and ',  self.y



#main program
p1 = Point(5, 7)
p1.setY(10)
print("Y Coord: ", p1.y)
print(p1.__str__())