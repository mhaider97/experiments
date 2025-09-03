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

random_floats_bw_2_and_3 = random_floats_bw_0_and_1 + 2.0
print("Floats B/W: ", random_floats_bw_2_and_3)

random_integers_between_100_and_250 = random_ints_bw_20_and_50 * 5
print("Ints B/W: ", random_integers_between_100_and_250)

# TASK 1 - Create Linear DataSet
# Your goal is to create a simple dataset consisting of a single feature and a label as follows:
# 1. Assign a sequence of integers from 6 to 20 (inclusive) to a NumPy array named feature.
# 2. Assign 15 values to a NumPy array named label such that:

feature = np.arange(6, 21)
print("Feature: ", feature)

label = (feature * 3) + 4
print("Label: ", label)

# TASk 2 - Add Some Noise to the Dataset
# To make your dataset a little more realistic, insert a little random noise into each element 
# of the label array you already created. To be more precise, modify each value assigned to 
# label by adding a different random floating-point value between -2 and +2.

# Don't rely on broadcasting. Instead, create a noise array having the same dimension as label.
noise = (np.random.random([15]) * 4) - 2
print("Noise: ", noise)

label = label + noise
print("Label: ", label)


