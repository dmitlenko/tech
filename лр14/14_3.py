def gen(n):
    from random import randint
    return [randint(-100,100) for i in range(n)]
def check(a):
    d = 0
    v = 0
    z = 0
    for i in a:
        if i > 0: d += 1
        elif i < 0: v += 1
        else: z += 1
    return d,v,z
n = int(input('n = '))
arr = gen(n)
d,v,z = check(arr)
print(*arr)
print("Додатніх: %i\nВід'ємних: %i\nНулів: %i\n"%(d,v,z))
