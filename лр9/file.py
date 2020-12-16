from random import *
N=randint(6,15)
A=[randint(-10,25) for i in range(N)]
print(A)

Arr2=[i for i in A if i>0]
print(Arr2) # больше нуля

Arr3=A
for i in range(N//2):
    Arr3[i],Arr3[N-1-i] = Arr3[N-1-i],Arr3[i]
print(Arr3) # реверс

for i in range(1,N,2):
    print(A[i],end=' ')
