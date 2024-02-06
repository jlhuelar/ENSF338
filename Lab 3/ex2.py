import timeit
import random


def bubble_sort(arr):
	n = len(arr)
	for i in range(n):
		for j in range(0, n-i-1):
			if arr[j] > arr[j+1]:
				temp = arr[j]
				arr[j] = arr[j+1]
				arr[j+1] = temp
	return arr

def quicksort(arr, low, high):
	if low < high:
		pivot_index=partition(arr, low, high)
		quicksort(arr, low, pivot_index)
		quicksort(arr, pivot_index + 1, high)

def partition(arr, low, high):
	pivot = arr[low]
	left = low + 1
	right = high
	done = False
	while not done:
		while left <= right and arr[left] <= pivot:
			left = left + 1
		while arr[right] >= pivot and right >= left:
			right = right - 1
		if right < left:
			done = True
		else:
            arr[left], arr[right] = arr[right], arr[left]
	arr[low], arr[right] = arr[right], arr[low]
	return right

def generate_random_array(size):
    return [random.randint(0, 10000) for _ in range(size)]

sizes = [10, 20, 50, 100, 200, 300, 400, 500, 600, 700, 800, 900, 1000, 1100, 1200, 1300, 1400, 1500, 1600, 1700]

results = []

def generate_random_array(size):
    return [random.randint(1, 10000) for _ in range(size)]

for size, bubble_time, quick_time in results:
    print(f"Size {size:>4}: Bubble sort took {bubble_time:.5f} seconds, Quicksort took {quick_time:.5f} seconds")
			