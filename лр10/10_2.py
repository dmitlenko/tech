from random import uniform
n = 5
m = 7
mat = []
for i in range(n):
    row = []
    for j in range(m): row.append(uniform(1.0,47.0))
    mat.append(row)
for i in range(n):
    for j in range(m):
        print(round(mat[i][j],1),end='\t')
    print()
ns1 = int(input('Введіть стовпець 1:'))
ns2 = int(input('Введіть стовпець 2:'))
if 0<=ns1<=n and 0<=ns2<=n:
    for sub in mat:
        sub[ns1],sub[ns2] = sub[ns2],sub[ns1]
else:
    print('Один або декілька стовпців не належать матриці')
for i in range(n):
    for j in range(m):
        print(round(mat[i][j],1),end='\t')
    print()
