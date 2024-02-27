# Optimized 'reverse()' implementation
def reverse_optimized(self):
    prev = None
    current = self.head
    while current:
        next_node = current.next
        current.next = prev
        prev = current
        current = next_node
    self.head = prev

import timeit
import matplotlib.pyplot as plt

# Basic singly-linked list implementation with both reverse functions
class ListNode:
    def __init__(self, value=0, next=None):
        self.value = value
        self.next = next
class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.size = 0
    
    def insert_tail(self, value):
        new_node = ListNode(value)
        if not self.head:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node
        self.size += 1
    
    def get_size(self):
        return self.size
    
    def reverse(self):
        newhead = None
        prevNode = None
        for i in range(self.get_size() - 1, -1, -1):
            currNode = self.get_element_at_pos(i)
            if newhead is None:
                newhead = currNode
            else:
                prevNode.next = currNode
            prevNode = currNode
        self.head = newhead
    
    def get_element_at_pos(self, pos):
        current = self.head
        for _ in range(pos):
            current = current.next
        return current
    
    def reverse_optimized(self):
        prev = None
        current = self.head
        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        self.head = prev

# Function to populate the list with n elements
def populate_list(lst, n):
    for i in range(n):
        lst.insert_tail(i)

# Sizes to test
sizes = [1000, 2000, 3000, 4000]

# Timing the reverse methods
original_times = []
optimized_times = []

# Adjusted timing with reduced repetitions for the original method on larger list sizes
original_times_adjusted = []
optimized_times_adjusted = []

# Define the number of repetitions for each list size for the original method
repetitions_original = {1000: 100, 2000: 100, 3000: 100, 4000: 100}

for size in sizes:
    lst = SinglyLinkedList()
    populate_list(lst, size)

    # Adjusted number of repetitions for the original method
    num_repetitions = repetitions_original[size]
    original_time_adjusted = timeit.timeit('lst.reverse()', globals=globals(), number=num_repetitions)
    original_times_adjusted.append(original_time_adjusted / num_repetitions * 1000)  # Scale to 1000 for comparison

    # Repopulate the list for the optimized method
    lst = SinglyLinkedList()
    populate_list(lst, size)

    # Timing the optimized reverse method with consistent 1000 repetitions
    optimized_time_adjusted = timeit.timeit('lst.reverse_optimized()', globals=globals(), number=1000)
    optimized_times_adjusted.append(optimized_time_adjusted)

# Plotting the adjusted timing results
plt.figure(figsize=(10, 6))
plt.plot(sizes, original_times_adjusted, label='Original Reverse (Adjusted Repetitions)', marker='o')
plt.plot(sizes, optimized_times_adjusted, label='Optimized Reverse', marker='s')
plt.xlabel('List Size')
plt.ylabel('Adjusted Time (seconds for 1000 reversals)')
plt.title('Adjusted Comparison of List Reversal Methods')
plt.legend()
plt.grid(True)
plt.show()
