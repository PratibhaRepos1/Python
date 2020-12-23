# List in Python
names = ["Jaz","Marks","Rampo","Julie", 2345, 'Hey', 45.56, True, 2*2]
print(names)
#insert a elements in list at particular position or index
names.insert(1,"Matt")
print(names)

#print particular index elements

print(names[3])

#del particular elements from List
del(names[3])
print(names)
print(len(names))
#replace element
names[0] ="John"
print(names)

#one more List

shoes =["Spizikes", "Air Force", "Curry","","", "Melo"]
print(shoes)

#update list
#Create a variable named shoes that is a list of the follow items, in order:

shoes =["Spizikes", "Air Force 1", "Curry 2", "Melo 5"]
print(shoes)


#Loops in Python
for shoe in shoes:
    print(shoe)

# range is not given a last number, its always give us 1 less than a particular range
for x in range(5,10):
    print(x)

#while Loops

i = 0

while i<=5:
    print(i)
    i += 1

#I have given you a list of ints called numbers. Print every number that is greater than 90.
print("Excerise")
numbers = [76, 83, 16, 69, 52, 78, 10, 77, 45, 52, 32, 17, 58, 54, 79, 72, 55, 50, 81,
74, 45, 33, 38, 10, 40, 44, 70, 81, 79, 28, 83, 41, 14, 16, 27, 38, 20, 84, 24, 50, 59,
 71, 1, 13, 56, 91, 29, 54, 65, 23, 60, 57, 13, 39, 58, 94, 94, 42, 46, 58, 59, 29, 69,
 60, 83, 9, 83, 5, 64, 70, 55, 89, 67, 89, 70, 8, 90, 17, 48, 17, 94, 18, 98, 72, 96, 26, 13,
  7, 58, 67, 38, 48, 43, 98, 65, 8, 74, 44, 92]

for n in numbers:
      if n > 90:
          print(n)

#Dictionaries

companies = {"Google":1990, "Amezon":1992, "Facebook":1998, "Netflix":2020}

print(companies)
companies["Netflix"]=2019
print(companies)

"""I have provided you with two lists. words and definitions

Create a dictionary called cooldictionary where you use words for keys and definitions for values
"""

words = ["PoGo","Spange","Lie-Fi"]
definitions = ["Slang for Pokemon Go",
"To collect spare change, either from couches, passerbys on the street or any numerous other ways and means",
"When your phone or tablet indicates that you are connected to a wireless network, however you are still unable to load webpages or use any internet services with your device"]

cooldictionary = {}
for i in range(0,3):
    cooldictionary[words[i]] = definitions[i]

print(cooldictionary)
