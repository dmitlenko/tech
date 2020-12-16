from random import randint

def calc(a,b,c,d,e):
    return (a + b + c + d + e) / 5

print('Результат:',calc(
    randint(2,10),
    randint(2,10),
    randint(2,10),
    randint(2,10),
    randint(2,10)
))
        
