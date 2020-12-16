from random import randint
s = 0
n = 3
m = 4
mat = []
for i in range(n):
    row = []
    for j in range(m):
        row.append(randint(-20,20))
    mat.append(row)

for i in range(n):
    for j in range(m):
        print(mat[i][j],end='\t')
    print()

print('sum =',sum(sum(mat,[])))
        
