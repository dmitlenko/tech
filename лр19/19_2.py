# l p h<- input
class V1:
    def __init__(self,v):
        self.v = v
class V2:
    def __init__(self,v):
        self.v = v
class Pool:
    def __init__(self,l,p,h):
        self.v = l * p * h
    def objects(self,v1,v2):
        self.v1 = V1(v1)
        self.v2 = V2(v2)
    def calculate(self):
        self.calculate = self.v - (3 * (self.v1.v - self.v2.v))
    def out(self):
        print("Об'єм води: %iл"%self.calculate)
        print("Ще може бути закачано: %i"%abs(self.v - self.calculate))
obj1 = Pool(int(input('l = ')),int(input('p = ')),int(input('h = ')))
obj1.objects(170,120)
obj1.calculate()
obj1.out()


