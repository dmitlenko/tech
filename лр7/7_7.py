x = float(input('x = '))
if x <= 0: y = 0
elif x > 0 and x <= 1: y = x*x
elif x > 1: y = x**4
print('f(x) = %f'%y)
