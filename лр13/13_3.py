nums = []
while True:
    inp = input('Число: ')
    if inp == ':': break
    else: nums.append(int(inp))
def isPlus(a):
    return a >= 0
for i in nums:
    print('Число %i додатнє: %s'%(i,isPlus(i)))
