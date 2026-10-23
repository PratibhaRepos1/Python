'''
Day 1: Variables & Data Types

Exercise 1: Personal Information
Create a Python program that:
- Stores your name in a variable.
- Stores your age as an integer.
- Stores your height in meters as a float.
- Stores whether you are learning Python as a boolean.
- Prints all four values.
- Prints the data type of each variable using type().

'''
name = "Pratibha"
age = 42
height = 1.55
learn_python = True

print("--------------- Exercise 1: Personal Information --------------------")
print("Name:", name)
print("Age:", age)
print("Height:", height)
print("Learning Python:", learn_python)

print(type(name))
print(type(age))
print(type(height))
print(type(learn_python))

'''
Exercise 2: Employee Salary Calculator
Easy
Create a program for an employee that:
- Stores the employee's name.
- Stores monthly salary as an integer.
- Stores bonus percentage as a float.
- Calculates the bonus amount.
- Calculates the total salary including the bonus.
- Prints the results.

'''
employee_name = "Alex"
salary = 50000
bonus = 10.0

bonus_amount = salary * bonus / 100
total_salary = salary + bonus_amount

print("--------------- Exercise 2: Employee Salary Calculator --------------------")
print("Employee: ", employee_name)
print("Monthly Salary:", salary)
print("Bonus Percentage:", bonus)

print("Bonus:", bonus_amount)
print("Total salary", total_salary)

'''
Exercise 3: AI Model Information

Imagine you're developing an AI application.

Create variables to store:
- AI model name: "GPT"
- Model version: 6
- Cost per million tokens: 2.50 (fictional practice value)
- Whether the model is active: True
Your program should:
1. Print all the values.
2. Print their data types.
3. Convert the model version from an integer to a string.
4. Print the data type after conversion.
Learning goal: Understand type conversion using str().

'''
model = "GPT"
version = 6
per_token_cost = 2.50
is_active = True


print("--------------- Exercise 3: AI Model Information --------------------")
print("model:", model)
print("version:", version)
print("per token cost:", per_token_cost)
print("active:", is_active)

print(type(model))
print(type(version))
print(type(per_token_cost))
print(type(is_active))

# Convert the model version from an integer to a string.
version = str(version)

print("After conversion data type of version ", type(version))
'''
Exercise 4: Shopping Bill Calculator
Medium
Create a Python program for a shopping bill.
Item	Price (THB)
Notebook	120
Pen	25
Python Book	450

Your program should:
1. Store each price in a separate variable.
2. Calculate the total price.
3. Apply a 10% discount.
4. Calculate the final amount after discount.
5. Print the original total, discount amount, and final amount.
6. Print the data type of the final amount.
Expected results: Original total = 595 THB; Discount = 59.50 THB; Final amount = 535.50 THB.

'''
item1 = "Notebook"
item1_price = 120
item2 = "Pen"
item2_price = 25
item3 = "Python Book"
item3_price = 450

discount = 10.0
total_price = item1_price + item2_price + item3_price
discount_amount = total_price * discount/100
final_amount = total_price - discount_amount

print("--------------- Exercise 4:  Shopping Bill Calculator --------------------")
print("Original total = ", total_price, "THB")
print("Discount = ", discount_amount, "THB")
print("Final amount = ", final_amount, "THB")

print("data type of final amount ", type(final_amount))


'''Exercise 5: Temperature Converter
Challenge
Create a Python program that converts a temperature from Celsius to Fahrenheit.

Requirements:
1. Store a Celsius temperature in a variable.
2. Convert it to Fahrenheit using the formula below.
3. Store the converted temperature in another variable.
4. Print both temperatures.
5. Print the data types of both variables.

'''
celsius_temp = 37.5
fahrenheit_temp = (celsius_temp * 9/5) + 32

print("--------------- Exercise 5: Temperature Converter --------------------")
print("Celsius: ", celsius_temp, "°C")
print("Fahrenheit: ", fahrenheit_temp, "°F")

print("Celsius temperature: ", type(celsius_temp))
print("Fahrenheit temperature: ", type(fahrenheit_temp))