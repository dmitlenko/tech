from random import random
class Shahtar:
    def __init__(self):
        self.command = "Шахтар"
class Dinamo:
    def __init__(self):
        self.command = "Динамо"
if random() > 0.5:
    obj = Shahtar()
else:
    obj = Dinamo()
print(obj.command,'вибирає поле.')
