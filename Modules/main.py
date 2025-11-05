# # Python Module is a file that contains built-in functions, classes,its and variables. 
# # There are many Python modules, each with its specific work.

# # Creation of simple, custom modules.
# # Importing Python modules into a program.
# # Using the from statement for selective importing.
# # Using an alias (e.g., import module as alias) to rename a module upon import

# # Create a Python Module : file calculator.py


# # Import module in Python
# # We can import the functions, and classes defined in a module to another module using the import statement in some other Python source file.

# # When the interpreter encounters an import statement, it imports the module if the module is present in the search path.

# # Note: A search path is a list of directories that the interpreter searches for importing a module.

# # For example, to import the module calc.py, we need to put the following command at the top of the script.

# # Syntax to Import Module in Python : import module (This does not import the functions or classes directly instead imports the module only. To access the functions inside the module the dot(.) operator is used.)

# #importing exp
# # importing  module calc.py
# import calculator

# print(f"importing  module calc.py = {calculator.add(10, 2)}")

# # Python Import From Module
# # Python's from statement lets you import specific attributes from a module without importing the module as a whole.

# # Import Specific Attributes from a Python module
# # Here, we are importing specific sqrt and factorial attributes from the math module.

# # importing sqrt() and factorial from the
# # module math
# from math import sqrt, factorial,pi

# # if we simply do "import math", then
# # math.sqrt(16) and math.factorial()
# # are required.
# print(sqrt(16))
# print(factorial(6))
# print(pi)

# # Import all Names 
# # The * symbol used with the import statement is used to import all the names from a module to a current namespace.

# # Syntax:

# # from module_name import *
# # What does import * do in Python?
# # The use of * has its advantages and disadvantages. If you know exactly what you will be needing from the module, it is not recommended to use *, else do so.

# # importing sqrt() and factorial from the
# # module math
# from math import *

# # if we simply do "import math", then
# # math.sqrt(16) and math.factorial()
# # are required.
# print(sqrt(16))
# print(factorial(6))


# #  Exersize
# # Unit Converter
# # Concept: Build a conversions.py module with functions to convert between different units (e.g., Celsius to Fahrenheit, inches to centimeters, kilometers to miles).
# # Main Program: Create a main script that prompts the user for a value and the desired conversion, then imports and calls the appropriate function from your conversions module.
# # Modules involved: No specific built-in modules are required, but it practices creating well-defined functions within a module

# # Password Generator
# # Concept: Develop a password_utils.py module that includes functions to generate strong, random passwords with customizable lengths and character types (letters, numbers, symbols).
# # Main Program: The main script would ask the user for their password preferences and then call the module's function to generate and display a new password.
# # Modules involved: random (for choosing random characters) and potentially the string module (to access sets of characters like string.ascii_letters, string.digits). 



# # Locating Python Modules
# # Whenever a module is imported in Python the interpreter looks for several locations. 
# # First, it will check for the built-in module, if not found then it looks for a list of directories defined in the sys.path.
# #  Python interpreter searches for the module in the following manner -

# # First, it searches for the module in the current directory.
# # If the module isn’t found in the current directory, Python then searches each directory in the shell variable PYTHONPATH.
# #  The PYTHONPATH is an environment variable, consisting of a list of directories.
# # If that also fails python checks the installation-dependent list of directories configured at the time Python is installed.
# # Directories List for Modules
# # Here, sys.path is a built-in variable within the sys module. It contains a list of directories that the interpreter will search for the required module.

# # importing sys module
# import sys

# # importing sys.path
# print(sys.path)


# # importing sqrt() and factorial from the
# # module math
# import math as mt

# # if we simply do "import math", then
# # math.sqrt(16) and math.factorial()
# # are required.
# print(mt.sqrt(16))
# print(mt.factorial(6))

# import random
# print(random.random())

# # importing built-in module math
# import math

# # using square root(sqrt) function contained 
# # in math module
# print(math.sqrt(25)) 

# # using pi function contained in math module
# print(math.pi) 

# # 2 radians = 114.59 degrees
# print(math.degrees(2))  

# # 60 degrees = 1.04 radians
# print(math.radians(60))  

# # Sine of 2 radians
# print(math.sin(2))  

# # Cosine of 0.5 radians
# print(math.cos(0.5))  

# # Tangent of 0.23 radians
# print(math.tan(0.23)) 

# # 1 * 2 * 3 * 4 = 24
# print(math.factorial(4))  

# # importing built in module random
# import random

# # printing random integer between 0 and 5
# print(random.randint(0, 5))  

# # print random floating point number between 0 and 1
# print(random.random())  

# # random number between 0 and 100
# holder = random.random() * 100
# print(holder) 
# print(holder+1) 

# List = [1, 4, True, 800, "python", 27, "hello"]

# # using choice function in random module for choosing 
# # a random element from a set such as a list
# print(random.choice(List)) 


# # importing built in module datetime
# import datetime
# from datetime import date
# import time

# # Returns the number of seconds since the
# # Unix Epoch, January 1st 1970
# print(time.time())  

# # Converts a number of seconds to a date object
# print(date.fromtimestamp(454554))


# JSON is a syntax for storing and exchanging data.

# JSON is text, written with JavaScript object notation.

# JSON in Python
# Python has a built-in package called json, which can be used to work with JSON data.

import json

# some JSON:
x =  '{ "name":"John", "age":30, "city":"New York"}'

# parse x:
y = json.loads(x)

# the result is a Python dictionary:
print(y["age"])


# Convert from Python to JSON
# a Python object (dict):
x = {
  "name": "John",
  "age": 30,
  "city": "New York"
}

# convert into JSON:
y = json.dumps(x)
print(type(x))
# the result is a JSON string:
print(y)
print(type(y))

# You can convert Python objects of the following types, into JSON strings:

# dict
# list
# tuple
# string
# int
# float
# True
# False
# None

import json

print(json.dumps({"name": "John", "age": 30}))
print(json.dumps(["apple", "bananas"]))
print(json.dumps(("apple", "bananas")))
print(json.dumps("hello"))
print(json.dumps(42))
print(json.dumps(31.76))
print(json.dumps(True))
print(json.dumps(False))
print(json.dumps(None))

print(x)
print(json.dumps(x, indent=4))
