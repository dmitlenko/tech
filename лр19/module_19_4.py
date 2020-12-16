from math import sqrt
class TriangleWorker:
    def __init__(self,a=1,b=1,c=1,t=0):
        if t == 0:
            self.size = (a,a,a)
        elif t == 1:
            self.size = (a,a,b)
        elif t == 2:
            self.size = (a,b,c)
    def perimeter(self):
        return sum(self.size)
    def area(self,t):
        side = self.size
        if t in [0,1,2]:
            return {
                0: round(side[0]/(2*sqrt(3))),
                1: round((side[1]/4)*sqrt(4 * side[0]**2 - side[1]**2)),
                2: round((side[0] * side[1]) / 2)
            }[t]
        else:
            return False
