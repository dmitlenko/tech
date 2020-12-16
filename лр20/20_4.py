test = {
    0:{
        't':'2 + 2 = 4?',
        'a':True
    },
    1:{
        't':'2 + 2 * 2 = 8?',
        'a':False
    },
    2:{
        't':'47 / 22 = 3?',
        'a':False
    },
    3:{
        't':'99 / 11 = 9',
        'a':True
    },
    4:{
        't':'22 + 7 - (18 * 22) = -367',
        'a':True
    },
}
i = 0
while True:
    try:
        print('\nПитання:',test[i]['t'])
        an = input('(правильно/не правильно) >')
        if (an == 'правильно' and test[i]['a'] == True) or (an == 'не правильно' and test[i]['a'] == False):
            i += 1
            print('Вірно!')
        elif not an in ('правильно','не правильно'):
            raise Exception('Введіть "правильно" або "не правильно"!')
        else:
            raise Exception('Не вірно! Спробуйте ще раз.')
    except Exception as e:
        print(e)
    if i == 5: break