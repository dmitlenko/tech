from random import random
arr = [random() for i in range(5)]
try:
    print(arr[8])
except IndexError:
    print('IndexError')
except ValueError:
    print('ValueError')