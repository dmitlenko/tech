from random import randint
randomNumber = randint(0,100)
win = False
attempts = 0
while attempts <= 10 and not win:
    num = int(input('Введіть число: '))
    if num == randomNumber:
        win = True
    elif num > randomNumber:
        print('менше')
    elif num < randomNumber:
        print('більше')
    attempts += 1
if win:
    print('Поздоровляємо Bи вгадали число з %i-ї спроби!'%attempts)
else:
    print('Спроби вичерпано :(\nЗагадане число було',randomNumber)
