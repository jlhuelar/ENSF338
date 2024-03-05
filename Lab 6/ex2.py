#   4. Based on BST and array search performances and running multiple trials, it can be concluded that BST approach is faster than the array approach.
#      For the trials, the total search time proved to be significantly faster using BST approach rather than the array approach.
#      Also for most cases, the average case times are faster using BST approach rather than the array approach

import random
import timeit

class Node:
    def __init__(self, data, parent=None, left=None, right=None):
        self.parent = parent
        self.data = data
        self.left = left
        self.right = right

def insert(data, root=None):
	current = root
	parent = None

	while current is not None:
		parent = current
		if data <= current.data:
			current = current.left
		else:
			current = current.right

	if root is None:
		root = Node(data)
	elif data <= parent.data:
		parent.left = Node(data, parent)
	else:
		parent.right = Node(data, parent)
		
def search(data, root):
	current = root
	while current is not None:
		if data == current.data:
			return current
		elif data < current.data:
			current = current.left
		else: current = current.right

	return None

array = []

def binary_search(arr, first, last, key):
    if first <= last:
        mid = (first + last) //2
        if key == arr[mid]: 
            return mid  # success: key found
        elif key < arr[mid]:
            return binary_search(arr, first, mid - 1, key)
        else:
            return binary_search(arr, mid + 1, last, key)
    return -1  # failure: key not found

vector = list(range(10000))
random.shuffle(vector)

bst_root = None
for number in vector:
    bst_root = insert(number, bst_root)

# Time the search for each element in the BST
bst_search_times = [timeit.timeit(lambda: search(element, bst_root), number=10) for element in vector]
average_bst_search_time = sum(bst_search_times) / len(bst_search_times)
total_bst_search_time = sum(bst_search_times)

# Now for the binary search on the array, we need to sort the array again because binary search requires sorted arrays
sorted_array = sorted(vector)
array_search_times = [timeit.timeit(lambda: binary_search(sorted_array, 0, len(sorted_array) - 1, element), number=10) for element in vector]
average_array_search_time = sum(array_search_times) / len(array_search_times)
total_array_search_time = sum(array_search_times)

(average_bst_search_time, total_bst_search_time, average_array_search_time, total_array_search_time)

print("BST Search Performance:")
print(f"Average search time: {average_bst_search_time} seconds")
print(f"Total search time for all elements: {total_bst_search_time} seconds")

print("\nArray Search Performance:")
print(f"Average search time: {average_array_search_time} seconds")
print(f"Total search time for all elements: {total_array_search_time} seconds")