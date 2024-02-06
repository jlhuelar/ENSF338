def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i  # Return the index of target
    return -1  # Target not found

def binary_search(arr, target):
    low, high = 0, len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            return mid  # Return the index of target
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1  # Target not found

def quicksort(arr):
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[-1]
        smaller, equal, larger = [], [pivot], []
        for x in arr[:-1]:
            if x < pivot:
                smaller.append(x)
            elif x > pivot:
                larger.append(x)
            else:
                equal.append(x)
        return quicksort(smaller) + equal + quicksort(larger)

# Implement the second algorithm: sort with quicksort then binary search
def sort_then_binary_search(arr, target):
    sorted_arr = quicksort(arr)  # Using the quicksort function defined earlier
    return binary_search(sorted_arr, target)

import matplotlib.pyplot as plt
import random
import time

# Function to generate a random array of a given size
def generate_random_array(size):
    return [random.randint(1, 1000) for _ in range(size)]

# Measure the performance of both algorithms
def measure_performance(num_tasks, array_size, target):
    linear_search_times = []
    quicksort_binary_search_times = []

    for _ in range(num_tasks):
        arr = generate_random_array(array_size)
        # Measure linear search time
        start_time = time.time()
        linear_search(arr, target)
        linear_search_times.append(time.time() - start_time)

        # Measure quicksort + binary search time
        start_time = time.time()
        sort_then_binary_search(arr, target)
        quicksort_binary_search_times.append(time.time() - start_time)

    # Calculate average times
    avg_linear_search_time = sum(linear_search_times) / num_tasks
    avg_quicksort_binary_search_time = sum(quicksort_binary_search_times) / num_tasks

    return avg_linear_search_time, avg_quicksort_binary_search_time

# Perform the measurement
num_tasks = 1000
array_size = 100  # Adjust the size to explore different scenarios
target = 500  # Constant element to search for
avg_linear_search_time, avg_quicksort_binary_search_time = measure_performance(num_tasks, array_size, target)

avg_linear_search_time, avg_quicksort_binary_search_time

# Define a function to measure performance for a range of input sizes
def measure_performance_for_sizes(input_sizes, num_tasks, target):
    results = {
        'size': [],
        'linear_search_time': [],
        'quicksort_binary_search_time': []
    }

    for size in input_sizes:
        avg_linear_search_time, avg_quicksort_binary_search_time = measure_performance(num_tasks, size, target)
        results['size'].append(size)
        results['linear_search_time'].append(avg_linear_search_time)
        results['quicksort_binary_search_time'].append(avg_quicksort_binary_search_time)
        print(f"Size: {size}, Linear: {avg_linear_search_time}, Quicksort+Binary: {avg_quicksort_binary_search_time}")

    return results

# Adjusted list of input sizes to test within computational limits
adjusted_input_sizes = [10, 20, 50, 100, 200, 500, 1000, 2000, 5000]

# Perform the measurements for the adjusted input sizes
adjusted_results = measure_performance_for_sizes(adjusted_input_sizes, num_tasks=10, target=500)  # Using 10 tasks for quicker execution

# Plot the results
plt.figure(figsize=(12, 8))

# Plotting linear search times
plt.plot(adjusted_results['size'], adjusted_results['linear_search_time'], label='Linear Search', marker='o')

# Plotting quicksort + binary search times
plt.plot(adjusted_results['size'], adjusted_results['quicksort_binary_search_time'], label='Quicksort + Binary Search', marker='s')

plt.xlabel('Input Size')
plt.ylabel('Average Execution Time (seconds)')
plt.title('Performance Comparison: Linear Search vs Quicksort + Binary Search')
plt.legend()
plt.xscale('log')
plt.yscale('log')
plt.grid(True, which="both", ls="--")
plt.show()
