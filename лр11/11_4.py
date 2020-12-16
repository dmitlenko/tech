a = input('Рядок -> ')
n = len(a) 
if n%2: mid = n//2 +1
else: mid = n//2
if a[mid:] == a[:mid][::-1]:
    print('Симетричний')
else:
    print('Несиметричний')
