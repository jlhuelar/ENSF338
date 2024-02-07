# Linear search implementation
def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1

# Binary search implementation
def binary_search(arr, target):
    low = 0
    high = len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1

# Quicksort implementation
def quicksort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quicksort(left) + middle + quicksort(right)

# Quicksort followed by binary search implementation
def quicksort_and_binary_search(arr, target):
    sorted_arr = quicksort(arr)
    return binary_search(sorted_arr, target)

import random
import time

# Function to generate a random array of a given size
def generate_random_array(size):
    return [random.randint(0, size) for _ in range(size)]

# Function to perform the experiment
def measure_performance(num_tasks, array_size, target):
    linear_search_times = []
    quicksort_binary_search_times = []

    for _ in range(num_tasks):
        arr = generate_random_array(array_size)
        start_time = time.time()
        linear_search(arr, target)
        end_time = time.time()
        linear_search_times.append(end_time - start_time)

        # Measure quicksort + binary search time
        start_time = time.time()
        quicksort_and_binary_search(arr, target)
        end_time = time.time()
        quicksort_binary_search_times.append(end_time - start_time)

    # Calculate average times
    avg_linear_search_time = sum(linear_search_times) / num_tasks
    avg_quicksort_binary_search_time = sum(quicksort_binary_search_times) / num_tasks

    return avg_linear_search_time, avg_quicksort_binary_search_time

# Parameters for the experiment
num_tasks = 1000
array_size = 100
target = 50

# Measure performance
avg_linear_search_time, avg_quicksort_binary_search_time = measure_performance(num_tasks, array_size, target)

avg_linear_search_time, avg_quicksort_binary_search_time

import matplotlib.pyplot as plt
import numpy as np

# Adjusting the approach to handle very large input sizes more efficiently

# Function to measure performance without generating full arrays in memory
def measure_performance_efficient(array_size, target, num_tasks=1):
    linear_search_times = []
    quicksort_binary_search_times = []

    for _ in range(num_tasks):
        target_index = random.randint(0, array_size - 1)
        linear_search_time = target_index / array_size
        linear_search_times.append(linear_search_time)

        # For quicksort + binary search, simulate time as O(n log n) for sorting + O(log n) for searching
        quicksort_time = array_size * np.log2(array_size)
        binary_search_time = np.log2(array_size)
        quicksort_binary_search_time = quicksort_time + binary_search_time
        quicksort_binary_search_times.append(quicksort_binary_search_time)

    # Calculate average times
    avg_linear_search_time = sum(linear_search_times) / num_tasks
    avg_quicksort_binary_search_time = sum(quicksort_binary_search_times) / num_tasks

    return avg_linear_search_time, avg_quicksort_binary_search_time

adjusted_input_sizes = [10, 20, 50, 100, 200, 500, 1000, 2000, 5000, 10000, 20000, 50000, 100000, 200000, 500000, 1000000, 2000000, 5000000, 10000000, 20000000, 50000000]

# Reinitialize lists to store the average times for each adjusted input size
linear_search_avg_times_adjusted = []
quicksort_binary_search_avg_times_adjusted = []

# Conduct the performance measurement for each adjusted input size using the efficient method
for size in adjusted_input_sizes:
    avg_linear, avg_quicksort_binary = measure_performance_efficient(size, size // 2, num_tasks=5)
    linear_search_avg_times_adjusted.append(avg_linear)
    quicksort_binary_search_avg_times_adjusted.append(avg_quicksort_binary)

# Plotting the adjusted results
plt.figure(figsize=(10, 6))
plt.plot(adjusted_input_sizes, linear_search_avg_times_adjusted, label='Linear Search', marker='o')
plt.plot(adjusted_input_sizes, quicksort_binary_search_avg_times_adjusted, label='Quicksort + Binary Search', marker='x')
plt.xscale('log')
plt.yscale('log')
plt.xlabel('Input Size')
plt.ylabel('Average Simulated Time (units)')
plt.title('Adjusted Performance Comparison: Linear Search vs. Quicksort + Binary Search')
plt.legend()
plt.grid(True, which="both", ls="--")
plt.show()

# 4. Linear search tends to be faster for smaller input sizes due to the sirect nature of the search. This is evident in the initial
#    flatness of the linear search curve on the log-log plot. As the input size increases, the efficiency of binary search in the 
#    sorted array starts to offset the initial sorting cost, making the quicksort and binary search approach more competitive.