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

x = np.array([[1, 2, 3],[3,4,8]])
y = np.array([4, 5, 6])

# Addition
add = x + y  
print("Addition:",add)



