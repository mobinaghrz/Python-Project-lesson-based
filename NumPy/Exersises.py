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
=================================

You're analyzing test scores for a class of students. Each student took 3 tests.

TASKS:
------
1. Calculate each student's average score (use np.mean with axis parameter)
2. Apply a "curve" to the averages: add the square root of each average to itself
   (use np.sqrt as a ufunc)
3. Sort the curved scores in DESCENDING order (highest to lowest)
4. Find how many students scored above 80 after the curve
5. Calculate the class average after the curve

BONUS CHALLENGE:
----------------
6. Return the original indices of the top 3 students (before sorting)
   Hint: Look up np.argsort()
"""

# Student test scores (rows = students, columns = test scores)
scores = np.array([
    [72, 85, 78],  # Student 0
    [90, 88, 92],  # Student 1
    [65, 70, 68],  # Student 2
    [78, 82, 75],  # Student 3
    [88, 91, 85],  # Student 4
    [55, 60, 58],  # Student 5
    [95, 98, 93],  # Student 6
    [70, 75, 72]   # Student 7
])


# Task 1: Calculate average for each student


# Task 2: Apply curve (add sqrt of average to the average)


# Task 3: Sort curved scores in descending order


# Task 4: Count students above 80


# Task 5: Calculate class average after curve


# Bonus Task 6: Find indices of top 3 students



# SOLUTION
# =========

# Task 1: Calculate average for each student
# axis=1 means calculate along each row (across columns)
averages = np.mean(scores, axis=1)
print("Task 1 - Original averages:")
print(averages)
print()

# Task 2: Apply curve (add sqrt of average to the average)
# np.sqrt is a ufunc that operates element-wise
curved_scores = averages + np.sqrt(averages)
print("Task 2 - Curved scores:")
print(curved_scores)
print()

# Task 3: Sort curved scores in descending order
# np.sort() sorts ascending by default, [::-1] reverses it
sorted_scores = np.sort(curved_scores)[::-1]
print("Task 3 - Sorted (descending):")
print(sorted_scores)
print()

# Task 4: Count students above 80
# curved_scores > 80 creates boolean array, np.sum counts True values
above_80 = np.sum(curved_scores > 80)
print(f"Task 4 - Students above 80: {above_80}")
print()

# Task 5: Calculate class average after curve
class_avg = np.mean(curved_scores)
print(f"Task 5 - Class average after curve: {class_avg:.2f}")
print()

# Bonus Task 6: Find indices of top 3 students
# np.argsort returns indices that would sort the array
# [::-1] reverses to get descending, [:3] takes first 3
top_3_indices = np.argsort(curved_scores)[::-1][:3]
print(f"Bonus - Top 3 student indices: {top_3_indices}")
print(f"Their curved scores: {curved_scores[top_3_indices]}")
print()

# Extra insight: Show the top 3 students' original scores
print("Top 3 students' original test scores:")
for idx in top_3_indices:
    print(f"  Student {idx}: {scores[idx]} → Average: {averages[idx]:.2f} → Curved: {curved_scores[idx]:.2f}")



    import numpy as np

"""
HOMEWORK: Monthly Sales Performance Analysis
=============================================

You're analyzing sales data for 6 salespeople over 4 months (Jan-Apr).
Each row represents a salesperson, each column represents a month.

TASKS:
------
1. Calculate total sales for each salesperson across all months
   (use np.sum with axis parameter)

2. Apply a 15% bonus to salespeople: multiply totals by 1.15
   (use direct multiplication - it's a ufunc!)

3. Calculate the square of each bonus amount (for tax calculations)
   (use np.square as a ufunc)

4. Sort the bonus amounts in ASCENDING order (lowest to highest)

5. Find how many salespeople have bonuses greater than $50,000

6. Calculate the average bonus amount for the team

BONUS CHALLENGE:
----------------
7. Find the indices of salespeople who earned less than $40,000 in bonuses
   Hint: Use boolean indexing with np.where()

8. Identify which salesperson had the highest single-month sale
   Hint: Use np.argmax() on the flattened array, then use np.unravel_index()
"""

# Monthly sales data (in thousands of dollars)
# Rows = Salespeople (0-5), Columns = Months (Jan-Apr)
sales = np.array([
    [12.5, 15.0, 18.2, 16.8],  # Salesperson 0
    [20.3, 22.1, 19.5, 21.7],  # Salesperson 1
    [8.5, 10.2, 9.8, 11.0],    # Salesperson 2
    [25.0, 28.5, 30.2, 27.8],  # Salesperson 3
    [14.8, 13.5, 16.0, 15.2],  # Salesperson 4
    [18.0, 19.5, 17.8, 20.2]   # Salesperson 5
])

print("Sales Data (in $1000s):")
print(sales)
print("\n" + "="*60 + "\n")

# YOUR CODE HERE
# ===============

# Task 1: Total sales for each salesperson


# Task 2: Apply 15% bonus


# Task 3: Square of bonus amounts


# Task 4: Sort bonuses in ascending order


# Task 5: Count bonuses > $50,000


# Task 6: Average bonus


# Task 7: Indices of salespeople with bonuses < $40,000


# Task 8: Salesperson and month with highest single sale




# =============================================================================
# SOLUTION BELOW - TRY IT YOURSELF FIRST!
# =============================================================================
# Task 1: Total sales for each salesperson
# axis=1 sums across columns (all months for each person)
total_sales = np.sum(sales, axis=1)
print("Task 1 - Total sales per salesperson (in $1000s):")
print(total_sales)
print()

# Task 2: Apply 15% bonus (multiply by 1.15)
# Direct multiplication is a ufunc operation
bonuses = total_sales * 1.15
print("Task 2 - Bonus amounts (in $1000s):")
print(bonuses)
print()

# Task 3: Square of bonus amounts
squared_bonuses = np.square(bonuses)
print("Task 3 - Squared bonuses:")
print(squared_bonuses)
print()

# Task 4: Sort bonuses in ascending order
sorted_bonuses = np.sort(bonuses)
print("Task 4 - Sorted bonuses (ascending):")
print(sorted_bonuses)
print()

# Task 5: Count bonuses > $50,000 (which is 50 in our data)
high_earners = np.sum(bonuses > 50)
print(f"Task 5 - Salespeople with bonuses > $50k: {high_earners}")
print()

# Task 6: Average bonus
avg_bonus = np.mean(bonuses)
print(f"Task 6 - Average bonus: ${avg_bonus:.2f}k")
print()

# Bonus Task 7: Indices of salespeople with bonuses < $40,000
low_earner_indices = np.where(bonuses < 40)[0]
print(f"Bonus 7 - Salespeople with bonuses < $40k: {low_earner_indices}")
print(f"         Their bonus amounts: ${bonuses[low_earner_indices]}k")
print()

# Bonus Task 8: Highest single-month sale
max_sale_flat_idx = np.argmax(sales)  # Index in flattened array
salesperson_idx, month_idx = np.unravel_index(max_sale_flat_idx, sales.shape)
month_names = ['January', 'February', 'March', 'April']
print(f"Bonus 8 - Highest single sale:")
print(f"         Salesperson {salesperson_idx} in {month_names[month_idx]}")
print(f"         Amount: ${sales[salesperson_idx, month_idx]}k")
print()

# Summary Display
print("="*60)
print("SUMMARY REPORT")
print("="*60)
for i in range(len(bonuses)):
    print(f"Salesperson {i}: Total=${total_sales[i]:.1f}k → Bonus=${bonuses[i]:.2f}k")
