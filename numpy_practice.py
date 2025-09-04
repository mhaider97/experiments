import numpy as np

# Numpy Google Colab
one_dimensional_array = np.array([1.2, 0.3, 1.5, 7.2, 2.1, 4.3])
print("1D: ", one_dimensional_array)

two_dimensional_array = np.array([[1, 2], [3, 4], [5, 6]])
print("2D: ", two_dimensional_array)

zeros_array = np.zeros([5])
print("Zeros: ", zeros_array)

ones_array = np.ones([5, 1])
print("ones: ", ones_array)

seq_integers = np.arange(10, 20)
print("Sequence: ", seq_integers)

random_ints_bw_20_and_50 = np.random.randint(low=20, high=51, size=(5))
print("Randoms: ", random_ints_bw_20_and_50)

random_floats_bw_0_and_1 = np.random.random((3,2))
print("Floats: ", random_floats_bw_0_and_1)

# Broadcasting, given operand will be operated to each element of the array based on the operation
random_floats_bw_2_and_3 = random_floats_bw_0_and_1 + 2.0 
print("Floats B/W: ", random_floats_bw_2_and_3)

random_integers_between_100_and_250 = random_ints_bw_20_and_50 * 5 
print("Ints B/W: ", random_integers_between_100_and_250)

# # Array Basic Operations
a = np.array([[1, 2, 3], [4, 5, 6]])
print("Example 2D Array: ", a)

print("Shape: ", a.shape)
print("Size: ", a.size)
print("Type: ", a.dtype)

# Reshape
print("Reshape: ", a.reshape(3, 2)) # Change the shape based on provided rows and columns

# Flatten
print("Flatten: ", a.ravel()) # Flatten the array

# Indexing
print("Slicing: ", a[0, 1])
print("Slicing: ", a[:, 1]) # It will take every row for 1st column

# Boolean indexing
print("Boolean Slicing: ", a[a > 3]) # Every element matching the expression will be taken

# # Maths Operations 
x = np.array([1, 2, 3])
y = np.array([4, 5, 6])
print("Example X: ", x)
print("Example Y: ", y)

print("Add: ", x + y)
print("Multiply: ", x * y)
print("Exponentiation: ", x ** 2)

# Broadcasting
m = np.ones((3, 3))
print("Ones Example: ", m)
print("Add in Ones", m + 5)

# Aggregations
print("Sum: ", np.sum(x))
print("Mean: ", np.mean(x))
print("Standard Deviation: ", np.std(x))
print("Min: ", np.min(x), "Max: ", np.max(x))
print("Arg Min: ", np.argmin(x), "Arg Max: ", np.argmax(x))

# Matrix multiplication
print("Dot: ", np.dot(x, y)) 
print(x @ y)

# # Array Functions
arr = np.array([3, 1, 2, 5, 4])
print("Example Array: ", arr)

print("Sorted: ", np.sort(arr))        
print("Arg Sorted: ", np.argsort(arr)) # Indices of the sorted elements

# Concatenation
a = np.array([1, 2])
b = np.array([3, 4])
print("Concat: ", np.concatenate([a, b]))

# Stack
print("Vertical Stack", np.vstack([a, b])) # Elements added vertically in a single column
print("Horizontal Stack", np.hstack([a, b])) # Elements added horizontally in a single row

# Split
c = np.array([1, 2, 3, 4, 5, 6])
print("Split: ", np.split(c, 3))   # Split into 3 parts

# Unique
print("Unique: ", np.unique([1, 2, 2, 3, 3, 3]))

# Copy vs View
arr1 = np.array([1, 2, 3])
arr2 = arr1.view() # Any change to this arr2 or arr1 will affect each other
arr3 = arr1.copy() # A new array, any change in this won't affect arr1
print(arr1, arr2, arr3)

# # Linear Algebra
M = np.array([[1, 2], [3, 4]])
print("Example Array: ", M)

print("Determinant: ", np.linalg.det(M)) # For small and medium sized matrices

sign, logdet = np.linalg.slogdet(M) # For large matrices
det = sign * np.exp(logdet) # To calculate determinant
print("Stable Determinant: ", det)

print("Inverse: ", np.linalg.inv(M))

vals, vecs = np.linalg.eig(M)
print("Eigenvalues: ", vals)
print("Eigenvectors: ", vecs)

# # Practical Examples
# TASK 1 - Create Linear DataSet
# Your goal is to create a simple dataset consisting of a single feature and a label as follows:
# 1. Assign a sequence of integers from 6 to 20 (inclusive) to a NumPy array named feature.
# 2. Assign 15 values to a NumPy array named label such that:

feature = np.arange(6, 21)
print("Feature: ", feature)

label = (feature * 3) + 4
print("Label: ", label)

# TASK 2 - Add Some Noise to the Dataset
# To make your dataset a little more realistic, insert a little random noise into each element 
# of the label array you already created. To be more precise, modify each value assigned to 
# label by adding a different random floating-point value between -2 and +2.

# Don't rely on broadcasting. Instead, create a noise array having the same dimension as label.
noise = (np.random.random([15]) * 4) - 2
print("Noise: ", noise)

label = label + noise
print("Label: ", label)

# TASK 3 - Simple Data Analysis
data = np.array([65, 70, 75, 80, 85, 90])
print("Example Array: ", data)

print("Mean: ", np.mean(data))
print("Std Dev: ", np.std(data))
print("Correlation: ", np.corrcoef(data, np.arange(len(data))))

# # Performance 
import time

n = 10**6
list1 = list(range(n))
list2 = list(range(n))

# Python loop
start = time.time()
result = [list1[i] + list2[i] for i in range(n)]
print("Python loop time taken: ", time.time() - start)

# NumPy vectorized
arr1 = np.arange(n)
arr2 = np.arange(n)
start = time.time()
result = arr1 + arr2
print("NumPy vectorized time taken: ", time.time() - start)