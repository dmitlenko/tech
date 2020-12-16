from math import sqrt
class Tri:
    def __init__(self,a,b,c):
        self.a,self.b,self.c = a,b,c
    def square(self):
        s = self.peri()/2
        return round(sqrt(s * (s - self.a) * (s - self.b) * (s - self.c)),2)
    def peri(self):
        return self.a + self.b + self.c
    def changeSide(self,a,b,c):
        self.a += a
        self.b += b
        self.c += c

class TriDouble(Tri):
    def square(self):
        s = self.peri()/2
        return round(sqrt(s * (s - self.a) * (s - self.a) * (s - self.c)),2)
    def peri(self):
        return (self.a * 2) + self.c
    def changeSide(self,a,b,c):
        Tri.changeSide(self,a,b,c)

obj1 = Tri(2,3,4)
obj2 = TriDouble(7,7,12)

print(obj1.square())
print(obj2.square())
obj1.changeSide(1,0,0)
obj2.changeSide(0,-3,0)
print(obj1.square())
print(obj2.square())
