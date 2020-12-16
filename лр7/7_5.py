month = int(input('Month:'))
print('Днів у %i-му місяці - '%month,end='') 
if month in [1,3,5,7,8,10,12]:
    print(31)
elif month == 2:
    print(29)
else:
    print(30)
