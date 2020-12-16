data = [ 2103.4, 4.2, 3092.7, 16989.8, 33.9, 1466.4, 81.0, 5363.1, 2414.9 ]
class Money:
    dat = []
    def __init__(self,new):
        self.dat = new
    def moneyFromComm(self):
        d = self.dat
        percent = (sum(d[0:4])/sum(d))*100
        return round(percent,2)
    def avgMoney(self):
        d = self.dat
        return round(sum(d)/len(d),2)
    def moneyFromInet(self):
        d = self.dat
        return round((d[7]/sum(d))*100,2)
obj = Money(data)
print('Bідсоток доходів за 4 види зв’язку від усіх доходів за півріччя:',obj.moneyFromComm())
print('Cередній дохід за півріччя:',obj.avgMoney())
print('Bідсоток інтернет-послуг від усіх доходів за півріччя:',obj.moneyFromInet())
