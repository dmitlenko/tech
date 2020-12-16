from random import randint
n = int(input('Размер -> '))
mat = []
for i in range(n):
    row = []
    for j in range(n):
        row.append(randint(10,99))
    mat.append(row)
    
print('До:')

for i in range(n):
    for j in range(n):
        print(mat[i][j],end='\t')
    print()

print('После:')

for i in range(n):
    for j in range(i):
        mat[j][i] = 0

for i in range(n):
    for j in range(n):
        print(mat[i][j],end='\t')
    print()
