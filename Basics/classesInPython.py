class Dog:
    dogInfo = "Hey dogs are cool"
    legs = 4
    def bark(self, str):
        print("BRAK! " + str)

myobj = Dog()
myobj.bark('running')

myobj.name = "JACK"
myobj.age = 3
print(myobj.name)
print(myobj.age)
print(Dog.dogInfo)
print(myobj.legs)

#another class
class Person:
    def __init__(self, name, age, furcolor):
        self.name = name
        self.age = age
        self.furcolor = furcolor


    def Display(self, str):
        print("Awesome! " + str)

myobjP = Person("Kale", 23, 'blue')
myobjP.Display('running')

print(myobjP.age)

#Excerise
"""Add a method to the Car class called age that returns how old the car is (2020 - year)

*Be sure to return the age, not print it*
"""

class Car:
    def __init__(self,year, make, model):
        self.year = year
        self.make = make
        self.model = model

    def age(self):
        return 2020 - self.year

objcar = Car(2018, 'Hundai', 'VXI')
mycarAgeIs = objcar.age()

print("Hey mycar, your age is {}".format(mycarAgeIs))
