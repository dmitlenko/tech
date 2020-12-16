from random import randint
n = m = 8
mat = []
for i in range(n):
    row = []
    for j in range(m):
        row.append(randint(1,100))
    mat.append(row)
mat1 = [row[:] for row in mat]
mat2 = [row[:] for row in mat]
mat3 = [row[:] for row in mat]
print('\n'.join([''.join(['%5d'%item for item in row]) for row in mat]))
print()
for i in range(n):
    for j in range(n-i):
        mat1[i][j] = 0
print('\n'.join([''.join(['%5d'%item for item in row]) for row in mat1]))
print()
for i in range(n):
    for j in range(i):
        mat2[i][j] = 0
print('\n'.join([''.join(['%5d'%item for item in row]) for row in mat2]))
print()
for i in range(n):
    for j in range(i):
        mat3[j][i] = 0
print('\n'.join([''.join(['%5d'%item for item in row]) for row in mat3]))
print()