a,b,c,d = (int(input('a = ')),int(input('b = ')),int(input('c = ')),int(input('d = ')))
if a>b>c>d:
    a = abs(a)
    b = abs(b)
    c = abs(c)
    d = abs(d)
elif a<b<c<d:
    a *= 10
    b *= 10
    c *= 10
    d *= 10
print('Вихідні значення:\na = %i\nb = %i\nc = %i\nd = %i'%(a,b,c,d))
