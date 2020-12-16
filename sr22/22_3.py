class Train:
    def timeToRun(self,num,time):
        if num == self.num:
            h1,m1 = self.time.split(':')
            h2,m2 = time.split(':')
            return (int(h1)-int(h2))*60 + (int(m1) - int(m2))
        else:
            return 0

class Rozklad(Train):
    num,nap,time = 0,"",""
    def __init__(self,n,na,t):
        self.num = n
        self.nap = na
        self.time = t

obj1 = Rozklad(17,"Днепр - Киев","14:40")
print(obj1.timeToRun(17,"12:27"))
