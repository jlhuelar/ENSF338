#   4. Worst-case complexity is O(n) for linear search when the element searched is the last element in an array
#      Worst-case is O(log n) for binary search when the element searched is the first, last or does not exist in an array

import timeit
import matplotlib.pyplot as plt
import numpy as np

#Inefficient Implementation
def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1  

#Efficient Implementation
def binary_search(arr, target):
    left = 0
    right = len(arr) - 1

    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return -1  

arr = sorted(np.random.randint(0, 100000, 1000))
target = np.random.choice(arr)

linear_setup = f"from __main__ import linear_search, arr, target"
binary_setup = f"from __main__ import binary_search, arr, target"

measurements = 100

linear_times = timeit.repeat("linear_search(arr, target)", setup=linear_setup, number=1, repeat=measurements)
binary_times = timeit.repeat("binary_search(arr, target)", setup=binary_setup, number=1, repeat=measurements)

average_linear_time = sum(linear_times) / len(linear_times)
average_binary_time = sum(binary_times) / len(binary_times)

print("Average Linear Search Execution Time:", average_linear_time)
print("Average Binary Search Execution Time:", average_binary_time)

plt.figure(figsize=(10, 6))
plt.hist(linear_times, alpha=0.5, label='Linear Search', bins=30)
plt.hist(binary_times, alpha=0.5, label='Binary Search', bins=30)
plt.xlabel('Execution Time (seconds)')
plt.ylabel('Frequency')
plt.title('Distribution of Execution Times for Linear vs. Binary Search')
plt.legend()
plt.show()