class Timer:
    hrs = 0
    mns = 0
    def __init__(self,h,m):
        self.hrs = h
        self.mns = m
    def all(self):
        return self.hrs * 60 + self.mns
print('Для завершенні введіть "!"')
while True:
    time = input('Введіть дані (пр. 22:30):')
    if time == '!':
        break
    else:
        time = time.split(':')
        obj  = Timer(int(time[0]),int(time[1]))
        print('Кількість хвилин:',obj.all())
