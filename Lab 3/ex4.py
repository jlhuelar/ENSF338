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

# Arrays of increasing size that will incur worst-case complexity for this implementation
# (since the last element, chosen as the pivot, is always the largest)
arrays = [
    [i for i in range(1, 6)],  # 5 elements
    [i for i in range(1, 11)],  # 10 elements
    [i for i in range(1, 16)],  # 15 elements
    [i for i in range(1, 21)],  # 20 elements
    [i for i in range(1, 26)]   # 25 elements
]

sorted_arrays = [quicksort(arr) for arr in arrays]
sorted_arrays

import matplotlib.pyplot as plt
import numpy as np

input_sizes = np.array([5, 10, 15, 20, 25])

theoretical_complexity = input_sizes ** 2

plt.figure(figsize=(10, 6))
plt.plot(input_sizes, theoretical_complexity, label='Theoretical Complexity $O(n^2)$', color='red', linestyle='--')
plt.scatter(input_sizes, input_sizes, label='Observed Complexity (Quicksort)', color='blue')

coefficients = np.polyfit(input_sizes, input_sizes, 2)
poly = np.poly1d(coefficients)
plt.plot(input_sizes, poly(input_sizes), label='Interpolated Observed Complexity', color='blue', linestyle=':')

plt.xlabel('Input Size')
plt.ylabel('Complexity (Arbitrary Units)')
plt.title('Quicksort Complexity Analysis')
plt.legend()
plt.grid(True)
plt.show()
