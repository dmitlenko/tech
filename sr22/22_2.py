class Time:
    h,m,s = 0,0,0
    def __init__(self,h,m,s):
        self.h = h
        self.m = m
        self.s = s
    def allSeconds(self):
        return self.h*3600 + self.m*60 + self.s
    def addSecond(self):
        self.s += 5
        if self.s >= 60:
            self.s -=60
            self.m += 1
        if self.m >= 60:
            self.m -= 60
            self.h += 1

obj1 = Time(22,44,12)
obj2 = Time(12,59,59)

print(obj1.allSeconds(),obj2.allSeconds())

obj1.addSecond()
obj2.addSecond()

print(obj1.allSeconds(),obj2.allSeconds())





        
