#class
"""class employee:
    id=1234
    name='subash'
    age=24
obj=employee()# it has the instance of the class
print(employee.id)#dot natation method
print(getattr,employee,'name')#getattribute method
setattr(employee,'name','sundar')#set attribute method
print(employee.name)
employee.name='asdf'# dot method value added
print(employee.name)
obj.age=23     # instance of the class is used in the change the object of the fields name
print(employee.age)
"""
# instance methods
"""class detail:
    name='subash'
    age=24
    def fun(self,gender):
        print("name is:",detail.name)
        print("age is :",detail.age)
o=detail()
o.fun('male')
"""
# constructor(init method)
# class employee:
#     def __init__(self,name):
#         self.name=name
#     def fun(self):
#         print('name is:',self.name)
# obj=employee('subash')
# obj.fun()
# obj1=employee('sundar')
# obj1.fun()
# obj2=employee('arun')
# obj2.fun()


# static method
# class employee:
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age
#     def fun(self):
#         print('name is:',self.name)
#         print("age is:",self.age)
#     @staticmethod
#     def sta():
#         print("welcome to all")
# obj=employee('subash',24)
# obj.fun()
# obj.sta()


# abstraction
# class stud:    #this pgm has one error
#     def ___init__(self,name):
#         self.name=name
    
#     def listname(self):
#         print("the name is available")
#         for name in self.name:
#             print(name)
    
#     def borrow_name(self,borrow_name):
#         if borrow_name in self.name:
#             print("your name is available")
#             self.name.remove (borrow_name)
#         else:
#             print("your name is not avaialable")
# name=['subash','sundar','asd','fgh']
# obj = stud(name)
# msg ="""
# 1.listname
# 2.borrow_name
# """
# while True:
#     print(msg)
#     ch=int(input("enter your choice"))
#     if ch==1:
#         o.listname()
#     elif ch==2:
#         name=input("enter name to borrow")
#         o.borrow_name(name)
#     else:
#         print("thank you come again")
# quit()


        
# inheritance (mutiple inherit)
# class A:
#     def cmp_a(self):
#         print("it is a software company")
# class B:
#     def cmp_b(self):
#         print("it is a product based company")
# class C(A,B):
#     def cmp_c(self):
#         print("it is a software product based company")
# o=C()
# o.cmp_a()
# o.cmp_b()
# o.cmp_c()

# over riding operator
# class emp:
#     def func(self):
#         self.a="asd"
#     def print1(self):
#         print("the value is",self.a)
# class emp1(emp):
#     def func(self):
#         self.a="sdd" 
#     def chng(self):# this has the overriding method
#         super().func()
# obj=emp()
# obj.func()
# obj.print1()

# o=emp1()
# o.func()
# o.chng()# this obj has declare
# o.print1()

# overloaded operator
# class a:
#     def __init__(self,a):
#         self.a=a
#     def __add__(b,c):
#         return b.a+c.a
# obj1=a(10)
# obj2=a(20)
# print("total:",(obj1+obj2))


# abstract method
from abc import ABC,abstractmethod
class bike(ABC):
    @abstractmethod
    def speed(self):
        pass
    def price(self):
        pass
class honda(bike):
    def speed(self):
        print("the honda bike speed is 91 kmph")
    def price(self):
        print("the honda bike price is 95000")
class pulsar(bike):
    def speed(self):
        print("the pulsar bike speed is 95 kmph")
    def price(self):
        print("the pulsar bike price is 100000")
obj=honda()
obj.speed()
obj.price()
obj1=pulsar()
obj1.speed()
obj1.price()
        