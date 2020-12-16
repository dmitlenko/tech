from random import randint
arr = [randint(5,55) for i in range(7)]
print(arr)
print('min ->',min(arr))
del arr[3]
print(arr)
arr.append(int(input('input -> ')))
print(arr)
print('min index ->',arr.index(min(arr)))
arr.insert(5,33)
print(arr)
arr.sort(reverse=True)
print(arr)
