from random import *
N = randint(6,15)
Arr = [randint(-10,25) for i in range(m)]
Arr2 = Arr
for i in range(N//2):
    Arr2[i],Arr2[N-1-i] = Arr[N-1-i],Arr2[i]
print('Revers:',*Arr2)
print('Parni index:',end=' ')
for i in range(0,N,2):
    print(Arr[i],end=' ')
print('Nevidyemni:',[i for i in Arr if i>0])

    

