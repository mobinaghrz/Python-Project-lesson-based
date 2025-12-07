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

# Using ndarray : The array object is called ndarray. NumPy arrays are created using the array() function. 

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


# Using Numpy Functions: NumPy provides convenient methods to create arrays initialized with specific values like zeros and ones:
import numpy as np

# Create a 1D array
arr1d = np.array([10, 20, 30, 40, 50])

# Single element access
print("Single element access:", arr1d[2])  

# Negative indexing
print("Negative indexing:", arr1d[-1])  

# Create a 2D array
arr2d = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

# Multidimensional array access
print("Multidimensional array access:", arr2d[1, 0])

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

# Slicing: Just like lists in Python, NumPy arrays can be sliced. As arrays can be multidimensional,
#  you need to specify a slice for each dimension of the array.


arr2 = arr[:2, ::2]
print ("first 2 rows and alternate columns(0 and 2):\n", arr2)
 
# Printing elements at specific Indices
# Advanced Indexing: Advanced Indexing in NumPy provides more flexible ways to access and manipulate array elements.

arr3 = arr[[1, 1, 0, 3], 
           [3, 2, 1, 0]]

print ("\nElements at indices (1, 3), "
    "(1, 2), (0, 1), (3, 0):\n", arr3)

# boolean array indexing 
cond = arr > 0
print ("\nElements greater than 0:\n", arr[cond])

print("-----------------------------------------\n")

# Data Types in Numpy
#  Every Numpy array is a table of elements (usually numbers), all of the same type, indexed by a tuple of positive integers.
#  Every ndarray has an associated data type (dtype) object. This data type object (dtype) provides information about the layout of the array.
#  The values of an ndarray are stored in a buffer which can be thought of as a contiguous block of memory bytes which can be interpreted 
# by the dtype object. Numpy provides a large set of numeric datatypes that can be used to construct arrays. At the time of Array creation,
#  Numpy tries to guess a datatype, but functions that construct arrays usually also include 
# an optional argument to explicitly specify the datatype.

# Constructing a Datatype Object
# In Numpy, datatypes of Arrays need not to be defined unless a specific datatype is required.
# Numpy tries to guess the datatype for Arrays which are not predefined in the constructor function.

import numpy as np
 
# Integer datatype
x = np.array([1, 2])  
print(x.dtype)         
 
# Float datatype
x = np.array([1.0, 2.0]) 
print(x.dtype)  
 
# Forced Datatype
x = np.array([1, 2], dtype = np.int64)   
print(x.dtype)


# Python NumPy

# Numpy is a general-purpose array-processing package. It provides a high-performance multidimensional array object, and tools for working with these arrays. It is the fundamental package for scientific computing with Python.

# Besides its obvious scientific uses, Numpy can also be used as an efficient multi-dimensional container of generic data.

# Arrays in Numpy
# Array in Numpy is a table of elements (usually numbers), all of the same type, indexed by a tuple of positive integers. In Numpy, number of dimensions of the array is called rank of the array. A tuple of integers giving the size of the array along each dimension is known as shape of the array. An array class in Numpy is called as ndarray. Elements in Numpy arrays are accessed by using square brackets and can be initialized by using nested Python Lists.

# Creating a Numpy Array
# Arrays in Numpy can be created by multiple ways, with various number of Ranks, defining the size of the Array. Arrays can also be created with the use of various data types such as lists, tuples, etc. The type of the resultant array is deduced from the type of the elements in the sequences.
# Note: Type of array can be explicitly defined while creating the array.




import numpy as np
 
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

# Output
# Array with Rank 1: 
#  [1 2 3]
# Array with Rank 2: 
#  [[1 2 3]
#  [4 5 6]]

# Array created using passed tuple:
#  [1 3 2]
# Accessing the array Index
# In a numpy array, indexing or accessing the array index can be done in multiple ways. To print a range of an array, slicing is done. Slicing of an array is defining a range in a new array which is used to print a range of elements from the original array. Since, sliced array holds a range of elements of the original array, modifying content with the help of sliced array modifies the original array content.




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

# Output
# first 2 rows and alternate columns(0 and 2):
#  [[-1.  0.]
#  [ 4.  6.]]

# Elements at indices (1, 3), (1, 2), (0, 1), (3, 0):
#  [0. 6. 2. 3.]
# Basic Array Operations
# In numpy, arrays allow a wide range of operations which can be performed on a particular array or a combination of Arrays. These operation include some basic Mathematical operation as well as Unary and Binary operations.




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

# Output
# Adding 1 to every element: [[2 3]
#  [4 5]]

# Subtracting 2 from each element: [[ 2  1]
#  [ 0 -1]]

# Sum of all array elements:  10

# Array sum:
#  [[5 5]
#  [5 5]]
# More on Numpy Arrays

# Basic Array Operations in Numpy
# Advanced Array Operations in Numpy
# Basic Slicing and Advanced Indexing in NumPy Python
# Data Types in Numpy
# Every Numpy array is a table of elements (usually numbers), all of the same type, indexed by a tuple of positive integers. Every ndarray has an associated data type (dtype) object. This data type object (dtype) provides information about the layout of the array. The values of an ndarray are stored in a buffer which can be thought of as a contiguous block of memory bytes which can be interpreted by the dtype object. Numpy provides a large set of numeric datatypes that can be used to construct arrays. At the time of Array creation, Numpy tries to guess a datatype, but functions that construct arrays usually also include an optional argument to explicitly specify the datatype.

# Constructing a Datatype Object
# In Numpy, datatypes of Arrays need not to be defined unless a specific datatype is required. Numpy tries to guess the datatype for Arrays which are not predefined in the constructor function.




import numpy as np
 
# Integer datatype
x = np.array([1, 2])  
print(x.dtype)         
 
# Float datatype
x = np.array([1.0, 2.0]) 
print(x.dtype)  
 
# Forced Datatype
x = np.array([1, 2], dtype = np.int64)   
print(x.dtype)

# Math Operations on DataType array
# In Numpy arrays, basic mathematical operations are performed element-wise on the array. 
# These operations are applied both as operator overloads and as functions.
#  Many useful functions are provided in Numpy for performing computations on Arrays such as sum: for addition of Array elements, T: for Transpose of elements, etc.
print("================================================")
import numpy as np
 
# First Array
arr1 = np.array([[4, 7], [2, 6]], 
                 dtype = np.float64)
                  
# Second Array
arr2 = np.array([[3, 6], [2, 8]], 
                 dtype = np.float64) 
 
# Addition of two Arrays
Sum = np.add(arr1, arr2)
print(Sum)
 
# Addition of all Array elements
Sum1 = np.sum(arr1)
print(Sum1)
 
# Square root of Array
Sqrt = np.sqrt(arr1)
print(Sqrt)
 
# Transpose of Array
Trans_arr = arr1.T
print(Trans_arr)

# Data type Object (dtype) in NumPy Python
# Last Updated : 11 Aug, 2021
# Every ndarray has an associated data type (dtype) object. This data type object (dtype) informs us about the layout of the array. 
# This means it gives us information about: 

# Type of the data (integer, float, Python object, etc.)
# Size of the data (number of bytes)
# The byte order of the data (little-endian or big-endian)
# If the data type is a sub-array, what is its shape and data type?
# The values of a ndarray are stored in a buffer which can be thought of as a contiguous block of memory bytes.
#  So how these bytes will be interpreted is given by the dtype object.  

# 1. Constructing a data type (dtype) object: A data type object is an instance of the NumPy.dtype class and it can be created using NumPy.dtype.

# Parameters: 

# obj: Object to be converted to a data-type object.
# align: bool, optional 
# Add padding to the fields to match what a C compiler would output for a similar C-struct.
# copy: bool, optional 
# Make a new copy of the data-type object. If False, the result may just be a reference to a built-in data-type object.


# Python Program to create a data type object 
import numpy as np 

# np.int16 is converted into a data type object. 
print(np.dtype(np.int16))



# Python Program to create a data type object 
# containing a 32 bit big-endian integer 
import numpy as np 

# i4 represents integer of size 4 byte 
# > represents big-endian byte ordering and < represents little-endian encoding. 
# dt is a dtype object 
dt = np.dtype('>i4') 

print("Byte order is:",dt.byteorder) 

print("Size is:",dt.itemsize) 

print("Data type is:",dt.name)

# The type specifier (i4 in the above case) can take different forms:

# b1, i1, i2, i4, i8, u1, u2, u4, u8, f2, f4, f8, c8, c16, a 
#    (representing bytes, ints, unsigned ints, floats, complex and 
#     fixed-length strings of specified byte lengths)
# int8,...,uint8,...,float16, float32, float64, complex64, complex128 
#    (this time with bit sizes)


# Note: dtype is different from type. 

# Python program to differentiate 
# between type and dtype. 
import numpy as np 

a = np.array([1]) 

print("type is: ",type(a)) 
print("dtype is: ",a.dtype)