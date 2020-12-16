from math import sqrt
def length(x1,y1,x2,y2):
    return sqrt((x2-x1)**2 + (y2-y1)**2)
p = lambda a,b,c: a+b+c
s = lambda p,a,b,c: sqrt((p/2)* ((p/2) - a) * ((p/2) - b) * ((p/2) - c))
x1,y1 = int(input('x1 ->')),int(input('y1 ->'))
x2,y2 = int(input('x2 ->')),int(input('y2 ->'))
x3,y3 = int(input('x3 ->')),int(input('y3 ->'))
a,b,c = length(x1,y1,x2,y2),length(x2,y2,x3,y3),length(x1,y1,x3,y3)
per = p(a,b,c)
print('Периметр:',per)
print('Площа:',s(per,a,b,c))
