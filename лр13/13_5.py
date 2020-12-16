from math import sqrt
def f(x):
    return (sqrt(x) + x + x**2) / (sqrt(x+1) + (x+1) + (x+1)**2)
def calc():
    val = 0
    for i in range(2,13,3):
        val += f(i)
    return val
print('Результат виразу:',calc())
