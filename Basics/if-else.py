# Simple if/else example - checking age for voting eligibility
age = 20

if age >= 18:
    print("You are eligible to vote!")
else:
    print("You are not eligible to vote yet!")


 # Using if/elif/else for grading
score = 75
 
if score >= 90:
    print("Grade A")
elif score >=80:
    print("Grade B")
elif score >= 70:
    print("Grade C")
elif score >=50:
    print("Grade D")
else:
    print("Grade F")

# different data types in Python
name = "Alice" # str (string) - text
myage = 34      # int (integer) - whole number
height = 5.1    # float - decimal number
is_student = True   # bool  - (boolean) - True/false

# checking the type of each variable

print(type(name))
print(type(myage))
print(type(height))
print(type(is_student))

if is_student:
    print(f"{name} is a student and is age {myage} years old")
else:
    print(f"{name} is not a student")
    
# Exercise 1: Even or Odd - Write a program that checks if a number is even or odd.

numbers = 20
if numbers % 2 == 0:
    print(f"Given number {numbers} is even")
else:
    print(f"Given number {numbers} is odd")

# Exercise 2: Data Type Detective Create four variables of different types (str, int, float, bool), then write if/else statements that print a different message depending on each variable's type


is_discount = 50.90


if type(is_discount) == int:
    print(f"This is integer type")
elif type(is_discount) == str:
    print("This is string type")
elif type(is_discount) == float:
    print("This is float type")
else:
    print("This is boolean")
    
# Exercise 3: Simple Login Check Create two variables, username and password. Write an if/else statement that prints "Login successful" only if username == "admin" and password == "1234". Otherwise print "Login failed".
username = "admin"
password = "1234"

if (username == "admin") and (password == "1234"):
    print("Login successful")
else:
    print("Login failed")

'''
Exercise 4: Number Classifier
Write a program that takes a number and prints whether it's positive, negative, or zero.

'''
num = input("enter your number:")

if int(num) > 0:
    print(f"The entered number {num} is positive")
elif int(num) < 0:
    print(f"The entered number {num} is negative")
else:
    print("The number is 0")

'''
Exercise 5: Type Conversion Challenge
age_text = "25"   # this is a string, not a number!
Convert age_text into an integer (hint: int()), then write an if/else that checks if the converted age is 18 or older.

'''
age_text = "5"
if int(age_text) >= 18:
    print("converted age is 18 or older")
else:
     print("converted age is  not 18 or older")