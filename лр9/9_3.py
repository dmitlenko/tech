from random import randint
arr = []
arr = [randint(-5,4) for i in range(20)]
print(*arr)
print('Позитивних значень:',len([x for x in arr if x>0]))
print('Нульових значень:',len([x for x in arr if x==0]))
