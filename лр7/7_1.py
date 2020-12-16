n = int(input('Скільки років:'))
p = int(input('Висота:'))
w = int(str(p)[-2:])
if (not (p > 30 and p < 200)) or (not (n >= 10 and n <= 100)):
    print('Введені невірні дані')
else:
    if n <= 25: o = w - 5
    elif n >= 25 and n <= 45: o = w
    else: o = w + 5  
    print('Oптимальна вага: %i kg'%o)

