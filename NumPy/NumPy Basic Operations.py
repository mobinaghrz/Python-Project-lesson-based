# NumPy Basic Operations
# Element-wise operations in NumPy allow you to perform mathematical operations on each element of an array individually,
#  without the need for explicit loops.

# Element-wise Operations: We can perform arithmetic operations like addition, subtraction, multiplication, 
# and division directly on NumPy arrays.

# Basic Array Operations
# In numpy, arrays allow a wide range of operations which can be performed on a particular array or a combination of Arrays.
#  These operation include some basic Mathematical operation as well as Unary and Binary operations.

import numpy as np

print("Basic Array Operations\n")

x = np.array([[1, 2, 3],[3,4,4]])
y = np.array([4, 5, 6])

# Addition
add = x + y  
print("Addition:",add)

print("-----------------------------------------\n Unary \n")

# Unary Operation: These operations are applied to each individual element in the array, 
# without the need for multiple arrays (as in binary operations).
# in other words it is an operation that takes one input and transforms it.

#  Note: unary operation works on a single operand (one array), unlike binary operations (like addition) that need two operands.
import numpy as np

# Example array with both positive and negative values
arr = np.array([-3, -1, 0, 1, 3])

# Applying a unary operation: absolute value
result = np.absolute(arr)
print("Absolute value:", result)

# other Importanr unary operations

# np.sqrt(arr) - square root
# np.square(arr) - square each element
# np.exp(arr) - exponential (e^x)
# np.log(arr) - natural logarithm
# np.negative(arr) - flip the sign

print("-----------------------------------------\n Binary Operation \n")
# Binary Operators: Numpy Binary Operations apply to the array elementwise and a new array is created. 
# We can use all basic arithmetic operators like +, -, /,  etc. In the case of +=, -=, = operators, the existing array is modified.

import numpy as np

# Two example arrays
arr1 = np.array([1, 2, 3])
arr2 = np.array([4, 5, 6])

# Applying a binary operation: addition
result = np.add(arr1, arr2)

print("Array 1:", arr1)
print("Array 2:", arr2)
print("Addition Result:", result)



print("-----------------------------------------\n ufuncs \n")
# NumPy ufuncs
# NumPy provides familiar mathematical functions such as sin, cos, exp, etc.
#  These functions also operate elementwise on an array, producing an array as output.

import numpy as np

# create an array of sine values
a = np.array([0, np.pi/2, np.pi])
print ("Sine values of array elements:", np.sin(a))

# exponential values
a = np.array([0, 1, 2, 3])
print ("Exponent of array elements:", np.exp(a))

# square root of array values
print ("Square root of array elements:", np.sqrt(a))


print("-----------------------------------------\n Sorting array \n")
# NumPy Sorting Arrays
# We can use a simple np.sort() method for sorting Python NumPy arr

import numpy as np

# set alias names for dtypes
dtypes = [('name', 'S10'), ('grad_year', int), ('cgpa', float)]

# Values to be put in array
values = [('Hrithik', 2009, 8.5), ('Ajay', 2008, 8.7), 
           ('Pankaj', 2008, 7.9), ('Aakash', 2009, 9.0)]
           
# Creating array
arr = np.array(values, dtype = dtypes)
print ("\nArray sorted by names:\n",
            np.sort(arr, order = 'name'))
            
print ("Array sorted by graduation year and then cgpa:\n",
                np.sort(arr, order = ['grad_year', 'cgpa']))


print("-----------------------------------------\n 2D Array \n")
# Visualizing Axes in a 2D Array
# Think of a 2D array like a table:

array = np.array([
    [12, 15, 18, 16],  # Row 0
    [20, 22, 19, 21],  # Row 1
    [8, 10, 9, 11]     # Row 2
])

# **Axis 0** = **down the rows** (vertical direction)  
# **Axis 1** = **across the columns** (horizontal direction)
# ```
#         Column 0  Column 1  Column 2  Column 3
#               ↓         ↓         ↓         ↓
# Row 0  →    [12,       15,       18,       16]
# Row 1  →    [20,       22,       19,       21]
# # Row 2  →    [8,        10,        9,       11]

#         ← Axis 1: across columns (→)
#         ↑ Axis 0: down rows (↓)

result = np.sum(array, axis=0)
# Sums each column: [12+20+8, 15+22+10, 18+19+9, 16+21+11]
# Result: [40, 47, 46, 48]
# Shape: (4,) - one sum per column
print(result)

result = np.sum(array, axis=1)
# Sums each row: [12+15+18+16, 20+22+19+21, 8+10+9+11]
# Result: [61, 82, 38]
# Shape: (3,) - one sum per row
print(result)
