def main():
    def showMenu():
        print('1. Задача 1')
        print('2. Задача 2')
        print('3. Задача 3')
        print('4. Задача 4')
        print('5. Задача 5')
        print('6. Exit')
    def task1(): # Задача 1
        from random import randint
        def ser(a,b,c):
            return (a+b+c)/3
        print('Середнє значення:',ser(randint(1,15),randint(1,15),randint(1,15)))
    def task2(): # Задача 2
        def maxi(a,b):
            return a if a>b else b

        def mini(a,b):
            return a if a<b else b
        x = int(input('x -> '))
        y = int(input('y -> '))
        print('( max(x,y) + min(x,y) )^2 ->',( maxi(x,y) + mini(x,y) )**2)
    def task3(): # Задача 3
        nums = []
        while True:
            inp = input('Число: ')
            if inp == ':': break
            else: nums.append(int(inp))
        def isPlus(a):
            return a >= 0
        for i in nums:
            print('Число %i додатнє: %s'%(i,isPlus(i)))
    def task4(): # Задача 4
        def generate():
            import random as rand
            a,b = rand.randint(0,9999999),rand.randint(0,999999)
            return a,b
        def enum(a,b):
            return a if len(str(a))>len(str(b)) else b 
        x,y = generate()
        big = enum(x,y)
        print('Числа:',x,y)
        print('Найбільше цифр:',big)
    def task5(): # Задача 5
        from math import sqrt
        def f(x):
            return (sqrt(x) + x + x**2) / (sqrt(x+1) + (x+1) + (x+1)**2)
        def calc():
            val = 0
            for i in range(2,13,3):
                val += f(i)
            return val
        print('Результат виразу:',calc())
    showMenu() #Вывод меню
    while True: # Главный цикл
        choose = int(input('> '))
        if choose == 6:
            break
        elif choose in range(1,6):
            exec('task%i()'%choose)

main()
    

