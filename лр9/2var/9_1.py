from random import *
Arr1 = [randint(-5,25) for i in range(8)]
Arr2 = [i for i in Arr1 if i%2!=0 and i<9]
print(*Arr1)
print(*Arr2)
