from random import randint
Mas1 = [randint(2,32) for i in range(10)]
Mas2 = [i for i in Mas1 if (i%2)==0 and i>10]
print(*Mas1,'\n',*Mas2)
