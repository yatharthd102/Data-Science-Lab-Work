# Lab 3 - NumPy
import numpy as np
# 1. Creating Arrays
arr1 = np.array([1, 2, 3, 4, 5])
arr2 = np.zeros((3, 3))
arr3 = np.ones((2, 4))
arr4 = np.arange(0, 20, 2)
arr5 = np.linspace(0, 1, 5)
print(arr1, arr4, arr5)
# 2. Array Properties
matrix = np.array([[1,2,3],[4,5,6],[7,8,9]])
print("Shape:", matrix.shape)
print("Dimensions:", matrix.ndim)
print("Size:", matrix.size)
# 3. Arithmetic Operations
a = np.array([10, 20, 30, 40, 50])
b = np.array([1, 2, 3, 4, 5])
print(a+b, a-b, a*b, a/b, a**2)
# 4. Statistical Functions
data = np.array([23, 45, 67, 12, 89, 34, 56, 78, 90, 11])
print(f"Mean:{np.mean(data):.2f}, Median:{np.median(data):.2f}")
print(f"Std:{np.std(data):.2f}, Min:{np.min(data)}, Max:{np.max(data)}")
# 5. Matrix Operations
A = np.array([[1, 2],[3, 4]])
B = np.array([[5, 6],[7, 8]])
print("Dot Product:\n", np.dot(A, B))
print("Transpose:\n", A.T)
print("Determinant:", np.linalg.det(A))
# 6. Indexing & Slicing
arr = np.array([[1,2,3,4],[5,6,7,8],[9,10,11,12]])
print("Row 0:", arr[0])
print("Col 2:", arr[:, 2])
print("Subarray:", arr[0:2, 1:3])
# 7. Boolean Indexing
scores = np.array([55, 78, 92, 45, 88, 63, 71])
print("Above 70:", scores[scores > 70])
print("Count:", np.sum(scores > 70))
