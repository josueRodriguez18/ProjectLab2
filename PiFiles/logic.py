import connection
import math
class Object(object):
    x = 0
    y = 0
    
class Field(object):
    
    RedTriangle = Object()
    RedSquare = Object()
    RedCircle = Object()

    BlueTriangle = Object()
    BlueSquare = Object()
    BlueCircle = Object()

    Ball = Object()
    
    
    

    def distance(self,ball, thing):
        x = ball.x - thing.x
        y = ball.y - thing.y
        dist = math.sqrt((pow(x, 2) + pow(y, 2)))
        return dist

    def closest(self):
            closest = self.RedTeam[0]
            for x in self.RedTeam:
                if(self.distance(self.Ball, x) < self.distance(self.Ball,closest)):
                    closest = x
            return closest
    
