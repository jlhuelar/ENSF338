# Linear search implementation
def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1

# Binary search implementation
def binary_search(arr, target):
    left, right = 0, len(arr) - 1

    while left <= right:
        mid = left + (right - left) // 2

        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return -1

# Timing and plotting code
import numpy as np
import timeit
from scipy.optimize import curve_fit
import matplotlib.pyplot as plt

def generate_sorted_vectors(sizes):
    return [sorted(np.random.randint(0, size * 10, size)) for size in sizes]

def linear_model(x, a, b):
    return a * x + b

def log_model(x, a, b):
    return a * np.log(x) + b

sizes = [1000, 2000, 4000, 8000, 16000, 32000]

sorted_vectors = generate_sorted_vectors(sizes)

linear_search_times = []
binary_search_times = []

for vector in sorted_vectors:
    linear_time = timeit.timeit(
        stmt='linear_search(vector, np.random.choice(vector))',
        globals=globals(),
        number=100) / 1000

    binary_time = timeit.timeit(
        stmt='binary_search(vector, np.random.choice(vector))',
        globals=globals(),
        number=100) / 1000

    linear_search_times.append(linear_time)
    binary_search_times.append(binary_time)

linear_params, _ = curve_fit(linear_model, sizes, linear_search_times)

binary_params, _ = curve_fit(log_model, sizes, binary_search_times)

linear_fit = linear_model(np.array(sizes), *linear_params)
binary_fit = log_model(np.array(sizes), *binary_params)

plt.figure(figsize=(14, 7))

plt.subplot(1, 2, 1)
plt.plot(sizes, linear_search_times, 'o', label='Measured Times')
plt.plot(sizes, linear_fit, '-', label='Linear Fit')
plt.title('Linear Search Performance')
plt.xlabel('Array Size')
plt.ylabel('Average Time (seconds)')
plt.legend()

plt.subplot(1, 2, 2)
plt.plot(sizes, binary_search_times, 'o', label='Measured Times')
plt.plot(sizes, binary_fit, '-', label='Logarithmic Fit')
plt.title('Binary Search Performance')
plt.xlabel('Array Size')
plt.ylabel('Average Time (seconds)')
plt.legend()

plt.tight_layout()
plt.show()

# 4. The interpolating function used for linear search is a linear function, which is represented mathematically by f(x) = ax + b. We
#    obtained values for a and b, which are the slope and y-intercept respectively, from the plotted curve. These  exact values depend
#    on the system and environment in which the tests were run, but a should generally be positive, reflecting a linear realtionship
#    which is visible on the plot. The results for linear search are as expected since the linear search algorithm's times complexity
#    is O(n) which means that the time taken to find an element scales linearly with the size of an array.
#    
#    For binary search, a logarithmic function was used for interpolation, which is represented by f(x) = alog(x) + b. The values of a
#    and b obtained from the curve indicates how closely the search times follow a logarithmic growth pattern. As with the linear search,
#    the specific values depend on the test conditions, but should show a positive a value, indicating an increase in time with larger
#    array sizes. The results for binary search also align with expectations since the binary search algorithm has a time complexity of
#    O(logn) which means that the time taken to find an element increases logarithmically as the array size increases.