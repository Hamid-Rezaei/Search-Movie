import numpy as np

print("Warm regards from the Cloud Computing TAs! Welcome to the Docker project.")
print()

print("We want to simply sort the elements in an array using NumPy in cc_hw2_hello.py")
array = np.array([
    [3, 7, 1],
    [10, 3, 2],
    [5, 6, 7]
])
print(f"The array:\n{array}")
print()

print("Sort the whole array:")
print(np.sort(array, axis=None))
print()

print("Sort along each row:")
print(np.sort(array, axis=1))
print()


print("Sort along each column:")
print(np.sort(array, axis=0))
    