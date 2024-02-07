import matplotlib.pyplot as plt
import numpy as np
import time

# Function to simulate linear search time based on O(n) complexity
def simulate_linear_search_time(array_size):
    return array_size

# Function to simulate quicksort (worst case) + binary search time based on O(n^2) + O(log n) complexity
def simulate_quicksort_worst_case_time(array_size):
    quicksort_worst_case_time = array_size ** 2
    binary_search_time = np.log2(array_size)
    return quicksort_worst_case_time + binary_search_time

# Define a range of input sizes
input_sizes = [10, 20, 50, 100, 200, 500, 1000, 2000, 5000, 10000]

# Lists to hold the simulated times
linear_search_times = []
quicksort_worst_case_times = []

# Calculate simulated times for each input size
for size in input_sizes:
    linear_search_times.append(simulate_linear_search_time(size))
    quicksort_worst_case_times.append(simulate_quicksort_worst_case_time(size))

# Plotting the results
plt.figure(figsize=(10, 6))
plt.plot(input_sizes, linear_search_times, label='Linear Search', marker='o')
plt.plot(input_sizes, quicksort_worst_case_times, label='Quicksort Worst Case + Binary Search', marker='x')
plt.xscale('log')
plt.yscale('log')
plt.xlabel('Input Size')
plt.ylabel('Simulated Time (units)')
plt.title('Simulated Performance: Linear Search vs. Quicksort Worst Case + Binary Search')
plt.legend()
plt.grid(True, which="both", ls="--")
plt.show()
