from math import sqrt
a,c = int(input('a = ')),int(input('c = '))
if a < 0:
    x1 = sqrt(-a)
    x2 = -c
    print('x1 = %f\nx2 = %f'%(x1,x2))
else:
    print('Pозв`язків немає')

