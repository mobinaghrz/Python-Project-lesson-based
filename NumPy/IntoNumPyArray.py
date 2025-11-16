#DEF: Numpy is a general-purpose array-processing package. 
# It provides a high-performance multidimensional array object, and tools for working with these arrays. 
# It is the fundamental package for scientific computing with Python.
# Besides its obvious scientific uses, Numpy can also be used as an efficient multi-dimensional container of generic data.

# Arrays in Numpy
# Array in Numpy is a table of elements (usually numbers), all of the same type, indexed by a tuple of positive integers.
#  In Numpy, number of dimensions of the array is called rank of the array.
#  A tuple of integers giving the size of the array along each dimension is known as shape of the array.
#  An array class in Numpy is called as ndarray.
#  Elements in Numpy arrays are accessed by using square brackets and can be initialized by using nested Python Lists.

# Creating a Numpy Array
# Arrays in Numpy can be created by multiple ways, with various number of Ranks, defining the size of the Array. 
# Arrays can also be created with the use of various data types such as lists, tuples, etc. 
# The type of the resultant array is deduced from the type of the elements in the sequences.
# Note: Type of array can be explicitly defined while creating the array.

import numpy as np
 
print("\nCreating a Numpy Array")
# Creating a rank 1 Array
arr = np.array([1, 2, 3])
print(arr)
 
# Creating a rank 2 Array
arr = np.array([[1, 2, 3],
                [4, 5, 6]])
print(arr)
 
# Creating an array from tuple
arr = np.array((1, 3, 2))
print(arr)

print("-----------------------------------------")

# Accessing the array Index
# In a numpy array, indexing or accessing the array index can be done in multiple ways.
# To print a range of an array, slicing is done.
# Slicing of an array is defining a range in a new array which is used to print a range of elements from the original array.
# Since, sliced array holds a range of elements of the original array, 
# modifying content with the help of sliced array modifies the original array content.

print("Accessing the array Index\n")

import numpy as np
 
arr = np.array([[-1, 2, 0, 4],
                [4, -0.5, 6, 0],
                [2.6, 0, 7, 8],
                [3, -7, 4, 2.0]])

# Printing a range of Array
# with the use of slicing method
arr2 = arr[:2, ::2]
print ("first 2 rows and alternate columns(0 and 2):\n", arr2)
 
# Printing elements at
# specific Indices
arr3 = arr[[1, 1, 0, 3], 
                [3, 2, 1, 0]]
print ("\nElements at indices (1, 3), "
    "(1, 2), (0, 1), (3, 0):\n", arr3)
print("-----------------------------------------")
