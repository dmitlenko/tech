class Conus:
    h,r = 0,0
    def __init__(self):
        print('Pадіус конуса може бути тільки додатнім числом')
    def calc(self):
        return round((
            int(self.__getattribute__('r')) *
            int(self.__getattribute__('h')) *
            3.14
        )/3,2)

obj = Conus()
for i in range(4):
    h = input('Висота %i-го конуса:'%(i+1))
    r = input('Радіус %i-го конуса:'%(i+1))
    obj.__setattr__('h',h)
    obj.__setattr__('r',r)
    print("Об'єм конуса:",obj.calc())
