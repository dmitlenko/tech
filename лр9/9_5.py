from random import randint
n = int(input('N:'))
a = [randint(0,200) for i in range(n)]
s = 0
for i in a:
    s += sum([int(x) for x in str(i)])
print(*a)
print('sum = ',s)
