from random import *
Arr = []
Arr = [randint(-6,3) for i in range(randint(6,15))]
print('Negativni:',[i for i in Arr if i<0])
print('Nulovi:',[i for i in Arr if i==0])
