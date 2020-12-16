class Book:
    title  = ""
    year   = 0
    author = ""
    def __init__(self,t,y,a):
        self.title,self.year,self.author = t,y,a
        print('Екземпляр створений')
    def allYear(self):
        return 2020 - self.year
    def __del__(self):
        print('Екземпляр знищений')
        self = None

class SuBook(Book):
    cost = 0
    def __init__(self,t,y,a,c):
        self.cost = c
        Book.__init__(self,t,y,a)
    def costByYear(self):
        y = self.allYear()
        if 5 <= y <= 10:
            self.cost *= 0.8
        elif y >= 10:
            self.cost *= 0.5
    def info(self):
        print('Назва:',self.title)
        print('Рік:',self.year)
        print('Автор:',self.author)
        print('Ціна:',self.cost,'грн.')

obj1 = SuBook('Велика Книга Знань',2012,'Махаон-Україна',315)
obj2 = SuBook('Pусские сказки',2009,'Ранок',210)
print(obj1.allYear(),obj2.allYear())
obj1.costByYear()
obj2.costByYear()
obj1.info()
obj2.info()
del obj1
del obj2
