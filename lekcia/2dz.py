for y in range(1,11):
    for x in range(1,11):
        if x==1 and y==1:
            print('',end='  ')
        elif y==1:
            print(x-1,end='  ')
        elif x==1:
            print(y-1,end='  ')
        else:
            print((x-1)*(y-1),end='  ')
    print('\n')
