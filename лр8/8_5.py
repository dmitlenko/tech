n = int(input("n = "))
suma = 0
for i in range(1,n+1):
    print(i)
    suma += i
if suma == (n*(n+1)/2): print("yes")
else: print("no")