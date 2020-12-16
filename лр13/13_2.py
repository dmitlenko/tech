def maxi(a,b):
    return a if a>b else b
def mini(a,b):
    return a if a<b else b
x = int(input('x -> '))
y = int(input('y -> '))
print('( max(x,y) + min(x,y) )^2 ->',( maxi(x,y) + mini(x,y) )**2)
