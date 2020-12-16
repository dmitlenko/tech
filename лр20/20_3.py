from random import randint
try:
    a = randint(0,100)
    be = randint(0,100)
    if a>b:
        print('a + b =',a+b)
    else:
        print('a * b =',a*b)
except NameError:
    print("Помилка виконання програми")