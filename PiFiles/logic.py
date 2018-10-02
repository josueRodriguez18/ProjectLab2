import connection
import math
class Object(object):
    def __init__(self):
        self.pos = [0,0]
        self.distance = 0
                    #Triangle Square Circle
    
class Field(object):
    corners = [0,0,0,0]
    center = [0,0]

    BlueTeam = [Object(), Object(), Object()]
                    #Triangle Square Circle
    RedTeam = [Object(), Object(), Object() ]
                    #Triangle Square Circle
    Ball = Object()
    def distance(self,ball, thing):
        x = ball.pos[0] - thing.pos[0]
        y = ball.pos[1] - thing.pos[1]
        dist = math.sqrt((pow(x, 2) + pow(y, 2)))
        return dist

    def closest(self):
            closest = self.RedTeam[0]
            for x in self.RedTeam:
                if(self.distance(self.Ball, x) < self.distance(self.Ball,closest)):
                    closest = x
            return closest
    
