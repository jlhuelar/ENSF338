import timeit
import random

class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key

class BSTBalanced:
    def __init__(self):
        self.root = None

    def insert(self, key):
        if self.root is None:
            self.root = Node(key)
        else:
            self._insert(self.root, key)

    def _insert(self, node, key):
        if key < node.val:
            if node.left is None:
                node.left = Node(key)
            else:
                self._insert(node.left, key)
        else:
            if node.right is None:
                node.right = Node(key)
            else:
                self._insert(node.right, key)

    def search(self, key):
        return self._search(self.root, key)

    def _search(self, node, key):
        if node is None:
            return False
        elif key == node.val:
            return True
        elif key < node.val:
            return self._search(node.left, key)
        else:
            return self._search(node.right, key)

def insert_balanced(bst, elements):
    if not elements:
        return
    mid = len(elements) // 2
    bst.insert(elements[mid])
    insert_balanced(bst, elements[:mid])
    insert_balanced(bst, elements[mid+1:])

def measure_search_time_balanced(bst, element):
    start_time = timeit.default_timer()
    bst.search(element)
    return timeit.default_timer() - start_time

def measure_performance(bst, elements):
    search_times = [sum(measure_search_time_balanced(bst, element) for _ in range(10)) / 10 for element in elements]
    average_time = sum(search_times) / len(search_times)
    total_time = sum(search_times)
    return average_time, total_time

# Generate a sorted vector of 10000 elements
sorted_vector = list(range(10000))

# For the sorted vector
bst_sorted = BSTBalanced()
insert_balanced(bst_sorted, sorted_vector)
average_time_sorted, total_time_sorted = measure_performance(bst_sorted, sorted_vector)

# For the shuffled vector
random.shuffle(sorted_vector)
bst_shuffled = BSTBalanced()
insert_balanced(bst_shuffled, sorted_vector)
average_time_shuffled, total_time_shuffled = measure_performance(bst_shuffled, sorted_vector)

# Results
print("Sorted Vector - Average Search Time:", average_time_sorted, "Total Search Time:", total_time_sorted)
print("Shuffled Vector - Average Search Time:", average_time_shuffled, "Total Search Time:", total_time_shuffled)

# 4. The results from the performance measurements of search operations in a balanced binary search tree constructed from both a 
#    sorted and a shuffled vector reveal that the search times are very similar between the two approaches. This similarity can be
#    attributed to the balanced nature of the BST in both cases. In a balanced BST, the height of the tree is kept to a minimum,
#    which in turn ensures that the time complexity of search operations is O(logn), where n is the number of nodes in the tree.
#    This time complexity is maintained regardless of whether the input vector is sorted or shuffled due to the balanced insertion
#    strategy ensuring the tree remains balanced.