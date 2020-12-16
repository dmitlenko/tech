from random import randint
class Expression:
    a = 0
    c = 0
    def __init__(self,a,c):
        self.a = a
        self.c = c
    def calc(self):
        return (self.a + self.c) ** 3

obj = Expression(randint(1,10),randint(-4,12))
print(obj.calc())
