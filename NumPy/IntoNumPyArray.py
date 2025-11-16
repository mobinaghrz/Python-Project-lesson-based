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