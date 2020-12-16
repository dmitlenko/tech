# l p <- input
class Book:
    def __init__(self,x,y):
        self.sq = x * y
class Sheet:
    def __init__(self,x,y):
        self.sq = x * y
class Table:
    def __init__(self,l,p):
        self.sq = l * p
    def objects(self,x1,y1,x2,y2):
        self.book = Book(x1,y1)
        self.sheet = Sheet(x2,y2)
    def calculate(self):
        self.calculate = self.sq - (self.book.sq + self.sheet.sq)
    def out(self):
        print('Книга і лист займають %icm^2'%(self.book.sq + self.sheet.sq))
        print('Вільного місця %icm^2'%self.calculate)

obj1 = Table(int(input('l = ')),int(input('p = ')))
obj1.objects(12,7,8,4)
obj1.calculate()
obj1.out()
