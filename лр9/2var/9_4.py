from random import *
N = int(input('N:'))
Arr = [randint(-50,50) for i in range(N)]
mi = Arr[0]
for i in range(N):
    if abs(Arr[i])<mi:
        mi = Arr[i]
print(*Arr)
print('min=',mi)
    
