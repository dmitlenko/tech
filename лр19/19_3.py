import module_19_3
obj1 = module_19_3.Module(int(input('from:')),int(input('to:')))
obj2 = module_19_3.Module(int(input('from:')),int(input('to:')))
obj3 = module_19_3.Module(int(input('from:')),int(input('to:')))

o1 = obj1.generate()
o2 = obj2.generate()
o3 = obj3.generate()

print("Середнє значення об'єкту 1:",obj1.avg())
print("Середнє значення об'єкту 2:",obj2.avg())
print("Середнє значення об'єкту 3:",obj3.avg())
