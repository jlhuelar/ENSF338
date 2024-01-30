def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1

def binary_search(arr, target):
    low = 0
    high = len(arr) - 1
    
    while low <= high:
        mid = (low + high) // 2
        guess = arr[mid]
        if guess == target:
            return mid
        if guess > target:
            high = mid - 1
        else:
            low = mid + 1
    return -1

import numpy as np
import timeit
import matplotlib.pyplot as plt

def measure_performance(arr_size):
    linear_times = []
    binary_times = []
    
    for _ in range(1000):
        arr = np.arange(arr_size)
        target = np.random.choice(arr)
        
        linear_time = timeit.timeit(lambda: linear_search(arr, target), globals=globals(), number=100)
        linear_times.append(linear_time)
        
        binary_time = timeit.timeit(lambda: binary_search(arr, target), globals=globals(), number=100)
        binary_times.append(binary_time)
    
    avg_linear_time = np.mean(linear_times)
    avg_binary_time = np.mean(binary_times)
    
    return avg_linear_time, avg_binary_time

sizes = [1000, 2000, 4000, 8000, 16000, 32000]

performance_results = []
for size in sizes:
    avg_linear, avg_binary = measure_performance(size)
    performance_results.append((size, avg_linear, avg_binary))

(performance_results)

from scipy.optimize import curve_fit

def linear_model(x, a, b):
    return a * x + b

def logarithmic_model(x, a, b):
    return a * np.log(x) + b

sizes = np.array([1000, 2000, 4000, 8000, 16000, 32000])
binary_times = np.array([result[2] for result in performance_results])

params_linear, _ = curve_fit(linear_model, sizes, binary_times)
params_log, _ = curve_fit(logarithmic_model, sizes, binary_times)

fitted_linear = linear_model(sizes, *params_linear)
fitted_log = logarithmic_model(sizes, *params_log)

plt.figure(figsize=(10, 6))

plt.plot(sizes, binary_times, 'bo', label='Binary Search Times')
plt.plot(sizes, fitted_log, 'g--', label='Logarithmic Fit')

plt.title('Binary Search Performance with Logarithmic Fit')
plt.xlabel('Array Size')
plt.ylabel('Average Time (seconds)')
plt.legend()
plt.grid(True)
plt.savefig('Lab 2/binary_search_log_fit.jpg')

'Lab 2/binary_search_log_fit.jpg'