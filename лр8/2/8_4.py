si = 0
s = 0
while True:
    inp = input('введіть число: ')
    if inp == '.': break
    else: s += int(inp)
    si += 1
print('Середнє арифметичне =',round(s/si,2))
