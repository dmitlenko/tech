inp = input()
inp = inp.replace('а', '%tmp%').replace('б', 'а').replace('%tmp%', 'б')
inp = inp.replace('А', '%tmp%').replace('Б', 'А').replace('%tmp%', 'Б')
print(inp)

