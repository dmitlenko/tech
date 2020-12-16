class OperatingSys:
    def __init__(self,n1="Операційна",n2="система"):
        sym = input('Символ: ')
        if sym == "L": print(n1,n2,"Linux")
        elif sym == "W": print(n1,n2,"Windows")
        else: print("Error!")

obj = OperatingSys()
