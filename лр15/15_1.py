class square:
    def sq(self,a):
        return a*a
        
sides = []
cl = square()

for i in range(5):
    sides.append(int(input('Строна квадрата %i: '%(i+1))))
for j in range(5):
    sides[j] = cl.sq(sides[j])
print('Площі квадратів:',*sides)
