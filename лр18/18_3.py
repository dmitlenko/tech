class Num:
    def __init__(self,a):
        self.a = a
    def __add__(self,other):
        self.a += other
    def __sub__(self,other):
        self.a -= other
    def __mul__(self,other):
        self.a *= other
    def __truediv__(self,other):
        self.a /= other
    def __str__(self):
        return '%s'%(round(self.a,2) if isinstance(self.a,float) else self.a)

a,b = float(input('a = ')),float(input('b = '))
obj = Num(a)
obj + b
print(obj)
obj - b
print(obj)
obj * b
print(obj)
obj / b
print(obj)

a,b = 'он','лайн'
obj = Num(a)
obj + b
print(obj)
obj * 4
print(obj)
