from random import randint
try:
    a = randint(0,100)
    b = randint(0,100)
    if a>b:
        eval("print('a + b =',a+b))")
    else:
        eval("print('a * b =',a*b))")
except SyntaxError as e:
    print("Помилка виконання програми")