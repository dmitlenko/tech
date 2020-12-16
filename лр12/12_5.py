arr = list(range(3,17,2))
print(arr)
print('5 ->',arr[5])
print('len ->',len(arr))
s = 0
for i in arr: s += i
print('sum ->',s)
arrP = [i + 1 for i in arr]
print(arrP)
print('arrP in arr ->',arrP in arr)
