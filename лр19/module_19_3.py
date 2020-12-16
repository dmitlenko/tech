from random import randint
class Module:
    def __init__(self,f,t):
        self.r = (f,t)
    def generate(self):
        self.generate = [randint(self.r[0],self.r[1]) for i in range(19)]
    def avg(self):
        return int(sum(self.generate)/len(self.generate))
