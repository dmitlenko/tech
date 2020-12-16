string = 'У майбутньому роль Інтернету в нашому житті буде тільки зростати, наближаючи нас до створення віртуальної реальності.'
print('Довжина ->',len(string)+1)
print('Кількість слів ->',len(string.split())+1)
string2 = string[19:27] + ' ' + string[56:64] + string[2:3] + string[22:23] + ' ' + chr(ord(string[33:34])+1)  + string[10:11]  + string[46:47]  + string[91:93] + string[64:66]  + string[66:76] + ' ' + string[2:3] + string[22:23] + string[24:26] + string[80:83] + ' ' + string[94:104] + chr(1043).lower()  + string[10:11] + ' '  + string[59:60]  + string[94:96] + string[97:99] 
print(string2)
