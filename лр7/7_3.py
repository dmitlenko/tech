m = int(input('Suma:'))
a,b,c = (int(input('a = ')),int(input('b = ')),int(input('c = ')))
if m <= a:
    o = 0
elif m > a and m <= b:
    o = m*0.1
elif m > b and m <= c:
    o = m*0.25
elif m > c:
    o = m/2
else:
    pass
print('Podatok:',int(o))
