# Creating classes in python
class MyClass:
    "Hello"
    defination = "This is class created by me" #class level variable

myobj = MyClass() #creating object
myobj1 = MyClass()
myobj1.name = "Pratibha" # instance level variable
print(myobj1.name)
print(myobj.defination)
print(myobj1.defination)
myobj1.name = "Pratibha Jadhav"
print(myobj1.name)

#Init - its a method in class
# def __init__(self): its a special method in class
# it works like Default constructor in c#
class Person:
    def __init__(self):
        print("Hey there")
p = Person()

class Employee:
    def __init__(self):
        "Hello"
    def __init__(self,name,id,address,salary):
        self.name=name
        self.id=id
        self.address = address
        self.salary = salary

emp = Employee("John", 1201,'M G Road', 12000)
print(emp.name)

#inheritance and class level methods example
class Car:
    def __init__(self,year, make, model):
        self.year = year
        self.make = make
        self.model = model

    def age(self):
        return 2016 - self.year
class Mustang(Car):
    def __init__(self, year):
        self.year=year
        self.make="Ford"
        self.model = "Mustang"

m = Mustang(2012)

print(m.age())
