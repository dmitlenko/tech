from random import randint
n = int(input('N:'))
arr = [randint(0,100) for i in range(n)]
m = arr[0] 
for x in range(n):
	if x%2==0 and x != 0:
	    if x > m: m = x
print(*arr)
print('max =',m) 
