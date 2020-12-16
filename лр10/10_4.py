n = int(input('n -> '))
m = int(input('m -> '))
mat = []
zeros = 0
for i in range(n):
    row = []
    for j in range(m):
        x = (i+j) if i < j else (i**2 - j**2)
        if x == 0: zeros += 1
        row.append(x)
    mat.append(row)
print('\n'.join([''.join(['%5d'%item for item in row]) for row in mat]))
print('Нулів:',zeros)

