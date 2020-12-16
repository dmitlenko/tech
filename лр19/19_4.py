import module_19_4 as modu
print('Меню:\n   1.Рівносторонній\n   2.Рівнобедрений\n   3.Прямокутний\n   4.Вихід')
while True:
    inp = int(input('Виб> '))
    if inp == 1:
        obj = modu.TriangleWorker(int(input('a = ')),t=0)
        print('Периметр:',obj.perimeter())
        print('Площа:',obj.area(0))
    elif inp == 2:
        obj = modu.TriangleWorker(int(input('a = ')),int(input('b = ')),t=1)
        print('Периметр:',obj.perimeter())
        print('Площа:',obj.area(1))
    elif inp == 3:
        obj = modu.TriangleWorker(int(input('a = ')),int(input('b = ')),int(input('c = ')),t=2)
        print('Периметр:',obj.perimeter())
        print('Площа:',obj.area(2))
    elif inp == 4:
        break
