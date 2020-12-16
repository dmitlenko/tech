class Ball:
    R = 0
    def setR(self,new):
        self.R = new
    def sq(self):
        return 4 * 3.14 * self.R ** 2
    def vol(self):
        return 1.33 * 3 * 3.14 * self.R ** 3

bal1 = Ball()
bal2 = Ball()

R = int(input('R = '))
bal1.setR(R)
bal2.setR(R)

print('Площа кулі:',bal1.sq())
print("Об'єм кулі:",bal2.vol())
