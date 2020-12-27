class OperatingSys:
    def __init__(self,n1="Операційна",n2="система"):
        sym = input('Символ: ')
        if sym == "L": self.p = n1 + ' ' + n2 + ' ' + "Linux"
        elif sym == "W": self.p =  n1 + ' ' + n2 + ' ' + "Windows"
        else: self.p =  "Error!"

obj = OperatingSys()
print(obj.p)