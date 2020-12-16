from random import randint
n = m = 5
mat = []
for i in range(n):
    row = []
    for j in range(m): row.append(randint(1,55))
    mat.append(row)

print('\n'.join([''.join(['%5d'%item for item in row]) for row in mat]))

s = 0
for i in range(n):
    s += mat[i][i]
    print('mat[%i][%i] = %i'%(i,i,mat[i][i]))
print('s =',s/n)
