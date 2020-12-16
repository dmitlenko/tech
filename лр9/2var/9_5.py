from random import *
Arr1 = [randint(-100,100) for i in range(40)]
Arr2 = [i for i in Arr1 if i>0]
print(*Arr1)
print(*Arr2)
