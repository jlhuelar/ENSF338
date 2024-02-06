import matplotlib.pyplot as plt
import numpy as np

def bubble_sort(arr):
	swaps = 0
	comparisons = 0
	n = len(arr)
	
	for i in range(n):
		for j in range(0, n-i-1):
			comparisons += 1
			if arr[j] > arr[j+1]:
				temp = arr[j]
				arr[j] = arr[j+1]
				arr[j+1] = temp
				swaps += 1
	return swaps, comparisons

input_sizes = range(1, 21)  # Adjust the range according to your needs
swaps_data = []
comparisons_data = []

for size in input_sizes:
    # Generate a random array of the given size
    arr = np.random.randint(100, size=size)  # Adjust the range of numbers according to your needs
    swaps, comparisons = bubble_sort(arr)
    swaps_data.append(swaps)
    comparisons_data.append(comparisons)

plt.figure(figsize=(10, 5))

# Plot for swaps
plt.subplot(1, 2, 1)
plt.plot(input_sizes, swaps_data, marker='o', linestyle='-', color='blue')
plt.title('Swaps by Input Size')
plt.xlabel('Input Size')
plt.ylabel('Number of Swaps')

# Plot for comparisons
plt.subplot(1, 2, 2)
plt.plot(input_sizes, comparisons_data, marker='o', linestyle='-', color='red')
plt.title('Comparisons by Input Size')
plt.xlabel('Input Size')
plt.ylabel('Number of Comparisons')

plt.tight_layout()
plt.show()