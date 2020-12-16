x,y = int(input("x => ")),int(input("y => "))
if x > y:
    maxi = x
    mini = y
elif y > x:
    maxi = y
    mini = x
else: maxi = mini = x
print("max^2(x,y) - min^2(x,y) ->",(pow(maxi,2) - pow(mini,2)))
