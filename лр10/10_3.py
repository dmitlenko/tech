from random import randint
n = int(input('n -> '))
m = int(input('m -> '))
s = 0
ma = 0
mat = []
for i in range(n):
    row = []
    for j in range(m): row.append(int(input('mat[%i][%i]='%(i,j))))
    mat.append(row)
for i in range(n):
    for j in range(m):
        print(mat[i][j],end='\t')
        if sum(mat[i]) > ma: ma = sum(mat[i])
    s += sum(mat[i])
    print('=',sum(mat[i]))
print('s   =',s)
print('max =',ma)
