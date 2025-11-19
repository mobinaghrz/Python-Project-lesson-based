# Arrays in Numpy

import numpy as np

# Creating a 1D array
x = np.array([1, 2, 3])

# Creating a 2D array
y = np.array([[1, 2], [3, 4]])

# Creating a 3D array
z = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])

print(x)
print(y)
print(z)


# Slicing: 

import numpy as np

arr = np.array([[1, 2, 3], [4, 5, 6]])
#elements from index 1 to 3
print("Range of Elements:",arr[0:3])

#all rows, second column
print("Multidimensional Slicing:", arr[:, 1])

# Second
import numpy as np
arr = np.array([10, 20, 30, 40, 50, 60, 70, 80, 90, 100])

# Integer array indexing 
indices = np.array([1, 3, 5])
print ("Integer array indexing:", arr[indices])

# boolean array indexing 
cond = arr > 0
print ("\nElements greater than 0:\n", arr[cond])



# NumPy Basic Operations

import numpy as np

x = np.array([1, 2, 3])
y = np.array([4, 5, 6])

# Addition
add = x + y  
print("Addition:",add)

# Subtraction
subtract = x - y 
print("substration:",subtract)

# Multiplication
multiply = x * y 
print("multiplication:",multiply)

# Division
divide = x / y  
print("division:", divide)

# Second 
import numpy as np
 
# Defining Array 1
a = np.array([[1, 2],
              [3, 4]])
 
# Defining Array 2
b = np.array([[4, 3],
              [2, 1]])
               
# Adding 1 to every element
print ("Adding 1 to every element:", a + 1)
 
# Subtracting 2 from each element
print ("\nSubtracting 2 from each element:", b - 2)
 
# sum of array elements
# Performing Unary operations
print ("\nSum of all array elements: ", a.sum())
 
# Adding two arrays
# Performing Binary operations
print ("\nArray sum:\n", a + b)


# Use any of these for an unarray operation
arr = np.array([-4, -1, 0, 1, 4])
print(np.sqrt(arr) ) #nan = not a number
print(np.square(arr))
print(np.exp(arr))
print(np.log(arr) )
print(np.negative(arr) )


# Applying a binary operation calculator 


# Ufunc and sort
import numpy as np

"""
EXERCISE: Student Grade Analysis
