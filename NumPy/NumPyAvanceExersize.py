"""
NUMPY STACKING, SPLITTING & BROADCASTING - PRACTICE EXERCISES

"""

import numpy as np

# ============================================================================
# PART 1: STACKING 
# ============================================================================

# Exercise 1.1: Create two arrays of shape (3,4) with values 1-12 and 13-24.
# Stack them to create: a) shape (6,4) b) shape (3,8) c) shape (3,4,2)





# Answer:
a = np.arange(1, 13).reshape(3, 4)
b = np.arange(13, 25).reshape(3, 4)
vertical = np.vstack((a, b))  # or np.concatenate((a,b), axis=0)
horizontal = np.hstack((a, b))  # or np.concatenate((a,b), axis=1)
depth = np.stack((a, b), axis=2)


# Exercise 1.2: You have monthly sales data for 4 products across 3 stores.
# Store1: [100, 150, 200, 120], Store2: [110, 160, 190, 130], Store3: [105, 155, 195, 125]
# Combine into single array and add a new store: [115, 165, 205, 135] as the last row.





# Answer:
store1 = np.array([100, 150, 200, 120])
store2 = np.array([110, 160, 190, 130])
store3 = np.array([105, 155, 195, 125])
store4 = np.array([115, 165, 205, 135])
all_stores = np.vstack((store1, store2, store3, store4))
# or: all_stores = np.array([store1, store2, store3, store4])


# Exercise 1.3: Create a 2D array [[1,2],[3,4]]. Add a column of row sums on the right
# and a row of column sums at the bottom. Final shape should be (3,3).





# Answer:
arr = np.array([[1, 2], [3, 4]])
row_sums = arr.sum(axis=1).reshape(-1, 1)  # [[3], [7]]
arr_with_col = np.hstack((arr, row_sums))
col_sums = arr_with_col.sum(axis=0)  # [4, 6, 10]
result = np.vstack((arr_with_col, col_sums))


# Exercise 1.4: Given arrays A(2,3), B(2,3), C(2,3), stack them to create shape (2,9)
# then reshape to (6,3). What's the difference between stacking then reshaping vs
# vstacking directly?





# Answer:
A = np.array([[1,2,3],[4,5,6]])
B = np.array([[7,8,9],[10,11,12]])
C = np.array([[13,14,15],[16,17,18]])
method1 = np.hstack((A, B, C)).reshape(6, 3)
method2 = np.vstack((A, B, C))
# method1 keeps rows together: [[1,2,3],[4,5,6],[7,8,9]...]
# method2 interleaves differently based on original structure


# ============================================================================
# PART 2: SPLITTING 
# ============================================================================

# Exercise 2.1: Create array of shape (4,12) with values 1-48.
# Split into 3 equal horizontal parts. Find the sum of each part.





# Answer:
arr = np.arange(1, 49).reshape(4, 12)
parts = np.hsplit(arr, 3)  # or np.array_split(arr, 3, axis=1)
sums = [part.sum() for part in parts]
# Each part is (4,4), sums: [312, 408, 504] or calculate manually


# Exercise 2.2: You have a dataset (6, 10) representing 6 samples with 10 features.
# Split it into training (first 4 samples) and testing (last 2 samples).
# Then split features into 2 groups of 5 features each.





# Answer:
data = np.random.randint(0, 100, (6, 10))
train, test = np.vsplit(data, [4])  # or data[:4], data[4:]
train_feat1, train_feat2 = np.hsplit(train, 2)
test_feat1, test_feat2 = np.hsplit(test, 2)


# Exercise 2.3: Create array (5, 15). Split horizontally at positions [3, 10] to get
# 3 parts of shapes (5,3), (5,7), (5,5). Verify the shapes.





# Answer:
arr = np.arange(75).reshape(5, 15)
part1, part2, part3 = np.hsplit(arr, [3, 10])
# or: np.array_split(arr, [3, 10], axis=1)
print(part1.shape, part2.shape, part3.shape)  # (5,3), (5,7), (5,5)


# Exercise 2.4: Given a 1D array of 20 elements, split it into 4 parts.
# Calculate: mean of part1, max of part2, min of part3, std of part4.





# Answer:
arr = np.arange(1, 21)
parts = np.array_split(arr, 4)
results = {
    'mean_p1': parts[0].mean(),
    'max_p2': parts[1].max(),
    'min_p3': parts[2].min(),
    'std_p4': parts[3].std()
}


# ============================================================================
# PART 3: BROADCASTING 
# ============================================================================

# Exercise 3.1: Array (4,3) contains test scores. Subtract mean of each row from
# that row (centering). Then divide each column by its standard deviation (scaling).





# Answer:
scores = np.array([[85, 90, 78], [92, 88, 95], [70, 75, 72], [88, 85, 90]])
row_means = scores.mean(axis=1).reshape(-1, 1)
centered = scores - row_means
col_stds = centered.std(axis=0)
scaled = centered / col_stds


# Exercise 3.2: You have prices array (3,4) for 3 stores and 4 products.
# Apply store-specific discounts [0.1, 0.15, 0.2] (per row).
# Then apply product-specific tax rates [0.05, 0.08, 0.06, 0.07] (per column).
# Calculate final prices: price * (1 - discount) * (1 + tax)





# Answer:
prices = np.array([[100, 120, 150, 80], [110, 125, 145, 85], [105, 115, 140, 82]])
discounts = np.array([0.1, 0.15, 0.2]).reshape(-1, 1)
taxes = np.array([0.05, 0.08, 0.06, 0.07])
final_prices = prices * (1 - discounts) * (1 + taxes)


# Exercise 3.3: Create coordinate grids. x from 0 to 3, y from 0 to 2.
# Calculate z = x² + y² for all combinations. Result should be shape (4, 3).





# Answer:
x = np.arange(4)
y = np.arange(3)
z = x[:, np.newaxis]**2 + y**2
# or using meshgrid:
# X, Y = np.meshgrid(x, y, indexing='ij')
# z = X**2 + Y**2


# Exercise 3.4: Array A is (5, 1, 4) and array B is (3, 4). 
# What will be the shape after A + B? Create example arrays and verify.





# Answer:
A = np.random.rand(5, 1, 4)
B = np.random.rand(3, 4)
result = A + B  # Shape will be (5, 3, 4)
# Broadcasting: (5,1,4) + (3,4) -> (5,1,4) + (1,3,4) -> (5,3,4)


# Exercise 3.5: Normalize a 2D array (4, 5) using: normalized = (X - min) / (max - min)
# Apply this per column (each column scaled independently to [0, 1] range).





# Answer:
X = np.random.randint(10, 100, (4, 5))
col_min = X.min(axis=0)
col_max = X.max(axis=0)
normalized = (X - col_min) / (col_max - col_min)


# ============================================================================
# CHALLENGE PROBLEMS (Combines all concepts)
# ============================================================================

# Challenge 1: Create 3 arrays of shape (2,4), (2,4), (2,4).
# Stack them vertically, split result into 2 parts vertically at position 3,
# then broadcast multiply first part by [1, 2, 3, 4] and second part by [2, 3, 4, 5].





# Answer:
arr1 = np.arange(1, 9).reshape(2, 4)
arr2 = np.arange(9, 17).reshape(2, 4)
arr3 = np.arange(17, 25).reshape(2, 4)
stacked = np.vstack((arr1, arr2, arr3))  # Shape (6, 4)
part1, part2 = np.vsplit(stacked, [3])
result1 = part1 * np.array([1, 2, 3, 4])
result2 = part2 * np.array([2, 3, 4, 5])


# Challenge 2: Create a distance matrix. Given points A at positions (1,2), (3,4), (5,6)
# and points B at positions (0,1), (2,3), calculate all pairwise Euclidean distances.
# Result shape should be (3, 2) where entry (i,j) is distance from A[i] to B[j].





# Answer:
A = np.array([[1, 2], [3, 4], [5, 6]])  # Shape (3, 2)
B = np.array([[0, 1], [2, 3]])  # Shape (2, 2)
# Using broadcasting:
diff = A[:, np.newaxis, :] - B[np.newaxis, :, :]  # Shape (3, 2, 2)
distances = np.sqrt((diff**2).sum(axis=2))  # Shape (3, 2)


# Challenge 3: You have RGB image data (3, 4, 3) - 3 rows, 4 cols, 3 color channels.
# Increase red channel by 20%, decrease green by 10%, keep blue same.
# Then apply brightness adjustment: row0: +10, row1: +20, row2: +15 to all channels.





# Answer:
image = np.random.randint(0, 256, (3, 4, 3))
channel_multipliers = np.array([1.2, 0.9, 1.0])
adjusted = image * channel_multipliers
brightness = np.array([10, 20, 15]).reshape(3, 1, 1)
final = adjusted + brightness
final = np.clip(final, 0, 255)  # Keep in valid range
















"""
NUMPY DATETIME & LINEAR ALGEBRA - PRACTICE EXERCISES

"""

import numpy as np

# ============================================================================
# PART 1: DATETIME OPERATIONS 
# ============================================================================

# Exercise 1.1: Create a date for your birthday in 2024. Extract and print
# the year, month, and day separately using datetime64 with different units.





# Answer:
birthday = np.datetime64('2024-05-15')
year = np.datetime64(birthday, 'Y')
month = np.datetime64(birthday, 'M')
day = np.datetime64(birthday, 'D')


# Exercise 1.2: Generate an array of all dates in March 2023.
# Count how many of these dates fall on weekdays (Monday-Friday).
# Hint: Use busday_count or check day of week manually.





# Answer:
march_dates = np.arange('2023-03-01', '2023-04-01', dtype='datetime64[D]')
weekdays = np.busday_count('2023-03-01', '2023-04-01')
# or: weekdays = sum(np.is_busday(march_dates))


# Exercise 1.3: Calculate the number of days, weeks, and years between
# '2020-01-01' and '2025-12-31'. Store results in a dictionary.





# Answer:
start = np.datetime64('2020-01-01')
end = np.datetime64('2025-12-31')
diff = end - start
result = {
    'days': diff,
    'weeks': np.timedelta64(diff, 'W'),
    'years': np.timedelta64(diff, 'Y')
}


# Exercise 1.4: You have project deadlines: ['2024-03-15', '2024-01-20', '2024-05-10', '2024-02-28']
# Sort them chronologically and find which deadline is closest to '2024-03-01'.





# Answer:
deadlines = np.array(['2024-03-15', '2024-01-20', '2024-05-10', '2024-02-28'], dtype='datetime64')
sorted_deadlines = np.sort(deadlines)
target = np.datetime64('2024-03-01')
distances = np.abs(deadlines - target)
closest = deadlines[np.argmin(distances)]


# Exercise 1.5: Create an array of the first day of every month in 2024.
# Then create another array showing the last day of each month.
# Hint: Use month arithmetic and date ranges.





# Answer:
first_days = np.arange('2024-01', '2025-01', dtype='datetime64[M]')
last_days = (first_days + 1) - np.timedelta64(1, 'D')
# or: last_days = np.arange('2024-01-31', '2025-01-01', dtype='datetime64[M]')


# Exercise 1.6: Given employee start dates: ['2020-06-15', '2021-03-10', '2019-11-20']
# and today's date '2024-02-15', calculate each employee's tenure in days.
# Filter employees who have worked more than 1000 days.





# Answer:
start_dates = np.array(['2020-06-15', '2021-03-10', '2019-11-20'], dtype='datetime64')
today = np.datetime64('2024-02-15')
tenure_days = today - start_dates
long_tenure = start_dates[tenure_days > np.timedelta64(1000, 'D')]


# Exercise 1.7: Generate business days (weekdays only) between '2024-01-01' and '2024-01-31'.
# How many business days are there? Exclude weekends.





# Answer:
business_days = np.busday_count('2024-01-01', '2024-02-01')
# or generate array:
all_days = np.arange('2024-01-01', '2024-02-01', dtype='datetime64[D]')
only_business = all_days[np.is_busday(all_days)]


# ============================================================================
# PART 2: LINEAR ALGEBRA - BASIC OPERATIONS 
# ============================================================================

# Exercise 2.1: Given matrix A = [[3,1,4],[1,5,9],[2,6,5]], calculate:
# a) rank, b) trace, c) determinant, d) check if matrix is singular (det=0)





# Answer:
A = np.array([[3, 1, 4], [1, 5, 9], [2, 6, 5]])
rank = np.linalg.matrix_rank(A)
trace = np.trace(A)
det = np.linalg.det(A)
is_singular = np.isclose(det, 0)


# Exercise 2.2: Create a 3x3 identity matrix. Raise it to the power of 5.
# What do you observe? Now create [[2,0,0],[0,2,0],[0,0,2]] and raise to power 3.





# Answer:
I = np.eye(3)
I_power = np.linalg.matrix_power(I, 5)  # Still identity
diagonal = np.array([[2, 0, 0], [0, 2, 0], [0, 0, 2]])
diagonal_power = np.linalg.matrix_power(diagonal, 3)  # [[8,0,0],[0,8,0],[0,0,8]]


# Exercise 2.3: Matrix B = [[4,2],[3,1]]. Calculate its inverse.
# Verify that B × B⁻¹ gives identity matrix (use np.allclose for comparison).





# Answer:
B = np.array([[4, 2], [3, 1]])
B_inv = np.linalg.inv(B)
identity_check = np.matmul(B, B_inv)
is_identity = np.allclose(identity_check, np.eye(2))


# Exercise 2.4: Calculate the eigenvalues and eigenvectors of matrix [[6,-2],[2,1]].
# Verify that for each eigenvalue λ and eigenvector v: A·v = λ·v





# Answer:
A = np.array([[6, -2], [2, 1]])
eigenvalues, eigenvectors = np.linalg.eig(A)
# Verification for first eigenvalue:
Av = np.dot(A, eigenvectors[:, 0])
lambda_v = eigenvalues[0] * eigenvectors[:, 0]
is_valid = np.allclose(Av, lambda_v)


# ============================================================================
# PART 3: LINEAR ALGEBRA - SOLVING SYSTEMS 
# ============================================================================

# Exercise 3.1: Solve the system of equations:
# 2x + 3y = 13
# 5x - y = 7
# Verify your solution by substituting back into the equations.





# Answer:
coefficients = np.array([[2, 3], [5, -1]])
constants = np.array([13, 7])
solution = np.linalg.solve(coefficients, constants)
# Verification:
check = np.allclose(np.dot(coefficients, solution), constants)


# Exercise 3.2: Solve the 3-equation system:
# x + y + z = 6
# 2x - y + 3z = 14
# 3x + 2y - z = 2





# Answer:
A = np.array([[1, 1, 1], [2, -1, 3], [3, 2, -1]])
b = np.array([6, 14, 2])
solution = np.linalg.solve(A, b)


# Exercise 3.3: Circuit analysis problem. Using Kirchhoff's laws:
# i1 + i2 = i3
# 5i1 + 10i2 = 20 (voltage loop 1)
# 10i2 + 15i3 = 30 (voltage loop 2)
# Solve for currents i1, i2, i3.





# Answer:
A = np.array([[1, 1, -1], [5, 10, 0], [0, 10, 15]])
b = np.array([0, 20, 30])
currents = np.linalg.solve(A, b)


# Exercise 3.4: Use least squares to fit a line y = mx + c to these points:
# x: [1, 2, 3, 4, 5]
# y: [2.1, 3.9, 6.2, 7.8, 10.1]
# Find m (slope) and c (intercept).





# Answer:
x = np.array([1, 2, 3, 4, 5])
y = np.array([2.1, 3.9, 6.2, 7.8, 10.1])
A = np.vstack([x, np.ones(len(x))]).T
m, c = np.linalg.lstsq(A, y, rcond=None)[0]


# Exercise 3.5: Fit a quadratic curve y = ax² + bx + c to points:
# x: [0, 1, 2, 3, 4]
# y: [1, 2.8, 8.9, 19.2, 33.5]
# Use least squares method.





# Answer:
x = np.array([0, 1, 2, 3, 4])
y = np.array([1, 2.8, 8.9, 19.2, 33.5])
A = np.vstack([x**2, x, np.ones(len(x))]).T
coeffs = np.linalg.lstsq(A, y, rcond=None)[0]  # [a, b, c]


# ============================================================================
# CHALLENGE PROBLEMS (Combines datetime and linear algebra)
# ============================================================================

# Challenge 1: You have stock prices for 5 consecutive business days starting '2024-01-02':
# prices = [100, 102, 98, 105, 103]
# Generate the date array (business days only). Fit a linear trend line.
# Predict the price on the 6th business day.





# Answer:
start = np.datetime64('2024-01-02')
dates = np.busday_offset(start, np.arange(5))
prices = np.array([100, 102, 98, 105, 103])
x = np.arange(5)
A = np.vstack([x, np.ones(5)]).T
m, c = np.linalg.lstsq(A, prices, rcond=None)[0]
predicted_price = m * 5 + c


# Challenge 2: Population growth model. Given population on dates:
# ['2020-01-01': 1000, '2021-01-01': 1100, '2022-01-01': 1220, '2023-01-01': 1340]
# Convert dates to days since 2020-01-01. Fit exponential model: P = P₀·e^(kt)
# Hint: Use log transform to make it linear, then lstsq.





# Answer:
dates = np.array(['2020-01-01', '2021-01-01', '2022-01-01', '2023-01-01'], dtype='datetime64')
populations = np.array([1000, 1100, 1220, 1340])
start_date = dates[0]
days = (dates - start_date).astype(int)
log_pop = np.log(populations)
A = np.vstack([days, np.ones(len(days))]).T
k, log_P0 = np.linalg.lstsq(A, log_pop, rcond=None)[0]
P0 = np.exp(log_P0)


# Challenge 3: Portfolio optimization. You have 3 stocks with return vectors over 4 periods:
# Stock A: [0.05, 0.03, -0.02, 0.04]
# Stock B: [0.02, 0.04, 0.01, 0.03]
# Stock C: [0.08, -0.01, 0.05, 0.02]
# Find weights [w1, w2, w3] that minimize variance while achieving target return of 0.035.
# Constraint: w1 + w2 + w3 = 1. Use covariance matrix and linear algebra.
# Hint: This is simplified - just calculate covariance and solve for equal contribution.





# Answer:
returns = np.array([[0.05, 0.03, -0.02, 0.04],
                    [0.02, 0.04, 0.01, 0.03],
                    [0.08, -0.01, 0.05, 0.02]])
cov_matrix = np.cov(returns)
mean_returns = returns.mean(axis=1)
# Simplified: equal weights that sum to 1
# For full optimization, use: scipy.optimize or analytical solution
A = np.vstack([mean_returns, np.ones(3)]).T
b = np.array([0.035, 1])
weights = np.linalg.lstsq(A, b, rcond=None)[0]