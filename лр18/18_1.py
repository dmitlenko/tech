from random import randint
class Num1:
    def func(self,arr):
        return sum(arr)/len(arr)
class Num2:
    def func(self,arr):
        p,n = 0,0
        for i in arr:
            if not i%2:
                p += 1
            else:
                n += 1
        return p,n
arr = [randint(-5,75) for i in range(7)]
obj1 = Num1()
obj2 = Num2()
print('Список:',*arr)
print('Середнє арифметичне:',obj1.func(arr))
print('Парних: %i\nНепарних: %i'%obj2.func(arr))
            
