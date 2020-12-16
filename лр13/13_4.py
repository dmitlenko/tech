def generate():
    import random as rand
    a,b = rand.randint(0,9999999),rand.randint(0,999999)
    return a,b
def lenth(a):
    count = 1
    x = 1
    for i in range(1,20):
        if a//x: count += 1
        x*=10
    return count
def enum(a,b):
    return a if lenth(a) > lenth(b) else b 
x,y = generate()
big = enum(x,y)
print('Числа:',x,y)
print('Найбільше цифр:',big)
