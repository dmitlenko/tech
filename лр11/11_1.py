inp = input('Рядок -> ')
if inp.islower() and (ord(inp) in range(ord('a'),ord('z') + 1 )):
    print('Нижній регістр')
elif inp.isupper() and (ord(inp) in range(ord('A'),ord('Z')+1)):
    print('Верхній регістр')
elif inp.isdigit():
    print('Число')
else:
    print('Ні те ні інше')
