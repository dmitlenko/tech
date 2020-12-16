from random import randint
n = randint(7,16)
A = [randint(-17,17) for i in range(n)]
print(*A)
print('Зворотній:',A[::-1])
print('Непарні індекси:',[x for x in A if (A.index(x)%2)!=0])
print('Менше нуля:',[x for x in A if x<0])
