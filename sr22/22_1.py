class Drib:
    a = 0
    b = 0
    def __init__(self,a,b):
        self.a = a
        self.b = b
    def percent(self):
        return round((self.a/self.b)*100,2)
    def bSum(self):
        s = str(self.b)
        if len(s) > 1:
            return sum([int(i) for i in list(s)])
        else:
            return self.b

obj1 = Drib(1,2)
obj2 = Drib(2,8)
obj3 = Drib(7,2)
obj4 = Drib(14,22)

print(obj1.percent(),obj1.bSum(),sep="\t")
print(obj2.percent(),obj2.bSum(),sep="\t")
print(obj3.percent(),obj3.bSum(),sep="\t")
print(obj4.percent(),obj4.bSum(),sep="\t")
