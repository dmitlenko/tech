ar = {'+','-','*','/'}
inp = input('Рядок -> ')
v = 0
for i in inp:
    if i in ar: v += 1
print('Кількість входжень:',v)
