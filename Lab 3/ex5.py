#   4. Based on the plot for the performance of both
#   binary insertion sort and traditional insertion sort,
#   binary insertion sort is faster because it finds the trys to
#   to implement the correct position for each element in an array


import matplotlib.pyplot as plt
import numpy as np
import time

def binary_search(arr, val, start, end):
    if start == end:
        if arr[start] > val:
            return start
        else:
            return start+1
 
    if start > end:
        return start
 
    mid = (start+end)//2
    if arr[mid] < val:
        return binary_search(arr, val, mid+1, end)
    elif arr[mid] > val:
        return binary_search(arr, val, start, mid-1)
    else:
        return mid


def binary_insertion_sort(arr):
    for i in range(1, len(arr)):
        val = arr[i]
        j = binary_search(arr, val, 0, i - 1)
        arr[j+1:i+1] = arr[j:i]  # Shift elements rightward
        arr[j] = val  # Insert val at its correct position

    return arr


def insertion_sort(arr):
	for i in range(1, len(arr)):
		val = arr[i]
		j = i-1
		while j >= 0 and val < arr[j]:
				arr[j + 1] = arr[j]
				j -= 1
		arr[j + 1] = val
            
input_sizes = range(100, 1001, 100)  # Array sizes from 100 to 1000, in steps of 100
times = []  # To store the time taken for each sort

times_insertion_sort = []
times_binary_insertion_sort = []

for size in input_sizes:
    # Generate a random array of the given size
    arr = np.random.randint(0, size, size)
    arr_copy = arr.copy()  # Make a copy for binary insertion sort
    
    # Time insertion sort
    start_time = time.time()
    insertion_sort(arr)
    times_insertion_sort.append(time.time() - start_time)
    
    # Time binary insertion sort
    start_time = time.time()
    binary_insertion_sort(arr_copy)
    times_binary_insertion_sort.append(time.time() - start_time)

# Plotting the results without spline interpolation
plt.figure(figsize=(12, 6))

plt.plot(input_sizes, times_insertion_sort, marker='o', linestyle='-', color='blue', label='Insertion Sort')
plt.plot(input_sizes, times_binary_insertion_sort, marker='x', linestyle='-', color='red', label='Binary Insertion Sort')

plt.title('Insertion Sort vs. Binary Insertion Sort Performance')
plt.xlabel('Input Size')
plt.ylabel('Time Taken (seconds)')
plt.legend()
plt.show()