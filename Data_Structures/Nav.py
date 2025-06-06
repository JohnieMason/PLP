# Features of Python
# (Open source, High level, Simple, object oriented, Expressive language, large standard library, GUI programming)
# Python used in building websites, creating games, crunching data, Making robots smart
# Data types: int(whole numbers), float(Decimal Numbers), str(Text), bool(True or false)

# EXAMPLE
# Variables hold data
age = 25           #int(integer)
height = 5.75      #float(decimal)
name = 'Charlie'   # str(string)
is_student = True  # Bool(boolean)

# print out the values
print("Name:", name)
print("Age:", age)
print("Height:", height)
print("Is a student:", is_student)

# CONTROL FLOW -MAKING DECISION
# Conditions used : if -else statements (Controls how our code runs)
# Example

temperature  = 30

if temperature > 25:
    print("It is a Hot day!")
else:
    print("It is a cool day")

# You can also add elif for multiple conditions. Example below;

# Grading system based on the marks
marks = 55
if marks > 70:
    print("Grade: Distinction")
elif marks >= 60:
    print("Grade: Credit")
elif marks >= 50:
    print("Grade: Pass")
else:
    print("Grade: Fail")

# LOOPS: Repeating loops like a pro!
# print numbers 0 to 4
#  (I) FOR LOOP
for i in range(10):
    print(i)  #Expected result: 0,1,2,3,4

 # (II) WHILE LOOP - Repeats as long as a condition is true.
countdown = 6

while countdown > 0:
    print("Counting down:", countdown)
    countdown -= 1

    print("Blast off!")


# LIST, TUPLES, SETS AND DICTIONARIES
# List - This is a collection of items i.e shopping list

fruits = ["Apple", "banana", "Cherry"]

#Accessing Elements
print(fruits[0])

# Modifying the elements
fruits[1] = "Orange"
print(fruits)

# Adding an Element
fruits.append("Grape")
print(fruits)

# TUPLES
# Tuples are like lists but UNCHAMGEABLE. (Once created, you can't modify it)
coordinates = (10, 20)
# Accessing the elements
print(coordinates[0])
# Trying to modify a tuple will raise an error
# coordinates[0] = 5 # Error! Tuples cannot be modified.

# SETS
# A set is a collection of unique items (no duplicates allowed)
unique_numbers = {1, 2, 2, 3, 4, 5}
print(unique_numbers)   
# You notice 2 is only printed once

# DICTIONARIES
# Store key-value pairs.
# A dictionary is like a phonebook - It stores key-value pairs.
student_info = {"name": "Charlie", "age": 21, "grade": "A"}
# Accessing a value by its key
print(student_info["name"])  # Outputs: Charlie
# Modifying a value
student_info["age"] = 22
print(student_info)  # Outputs: {'name': 'Charlie', 'age': 22, 'grade': 'A'}

# FUNCTIONS
# Functions are blocks reusable code - just like superpowers you can call whenever you need them.

# Defining a function
def greet(name):
    print("Hello, " + name + "!👋")

# Calling the function
greet("Alice")
greet("Tamara")

# Return values
# Functions can return values
def add_numbers(x, y):
    return x + y
result = add_numbers(10, 5)
print(result) 

# Modules (Math Module)
# These are specialized code libraries that you can use without building everything form scratch.
# Its like using a TOOLBOX instead of crafting tools from scratch.
import math
# using the math module to calculate the square root 
print(math.sqrt(16)) #Output: 4

# Random Module
import random
# Generate a random number between 1 and 6 (like rolling a die)
dice_roll = random.randint(1, 6)
print("You a rolled a", dice_roll)








