from random import randint
class Parent:
    def meth1(self):
        return self.a * self.b
    def meth2(self):
        return self.a + self.b
class Child(Parent):
    def out(self):
        print("%i * %i ="%(self.a,self.b),self.meth1())
        print("%i + %i ="%(self.a,self.b),self.meth2())
obj1 = Child()
obj1.a, obj1.b = randint(-5,12),randint(-5,12)
obj1.out()
