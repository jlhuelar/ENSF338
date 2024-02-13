# Linked List Class
class ListNode:
    def __init__(self, value=0, next=None):
        self.value = value
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = None
    
    def append(self, value):
        if not self.head:
            self.head = ListNode(value)
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = ListNode(value)

    def to_sorted_array(self):
        arr = []
        current = self.head
        while current:
            arr.append(current.value)
            current = current.next
        arr.sort()
        return arr
    
    def binary_search(self, num):
        arr = self.to_sorted_array()
        left, right = 0, len(arr) - 1
        while left <= right:
            mid = (left + right) // 2
            if arr[mid] == num:
                return True
            elif arr[mid] < num:
                left = mid + 1
            else:
                right = mid - 1
        return False

# Array Class with Binary Search    
class Array:
    def __init__(self):
        self.array = []

    def append(self, value):
        self.array.append(value)
        self.array.sort()

    def binary_search(self, num):
        arr = self.to_sorted_array()
        left, right = 0, len(arr) - 1
        while left <= right:
            mid = (left + right) // 2
            if arr[mid] == num:
                return True
            elif arr[mid] < num:
                left = mid + 1
            else:
                right = mid - 1
        return False
    
# 4. Binary search on a linked list is less efficient than binary search on an array. For a linked list, the operation of accessing
#    the middle element is not O(1) as it is for arrays, but O(n) for the worst case as you have to traverse the list from the
#    beginning to reach the middle element. While the binary search divides the search space in half with each step, the need to
#    traverse the list to find the middle element results in an overall complexity of O(nlogn) for binary search on a linked list.
#    This is because of the O(n) traversal operation.
    
import time
import matplotlib.pyplot as plt
import numpy as np

class ListNode:
    def __init__(self, value=0, next=None):
        self.value = value
        self.next = next

class LinkedList:
    def __init__(self, values=None):
        self.head = None
        if values:
            for value in values:
                self.append(value)
    
    def append(self, value):
        if not self.head:
            self.head = ListNode(value)
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = ListNode(value)

    def binary_search(self, num):
        arr = self.to_sorted_array()
        left, right = 0, len(arr) - 1
        while left <= right:
            mid = (left + right) // 2
            if arr[mid] == num:
                return True
            elif arr[mid] < num:
                left = mid + 1
            else:
                right = mid - 1
        return False

    def to_sorted_array(self):
        arr = []
        current = self.head
        while current:
            arr.append(current.value)
            current = current.next
        return arr

class Array:
    def __init__(self, values=None):
        self.array = values if values else []
        self.array.sort()
    
    def binary_search(self, num):
        left, right = 0, len(self.array) - 1
        while left <= right:
            mid = (left + right) // 2
            if self.array[mid] == num:
                return True
            elif self.array[mid] < num:
                left = mid + 1
            else:
                right = mid - 1
        return False

def measure_performance(cls, sizes, num_searches=100):
    times = []
    for size in sizes:
        data = list(range(size))
        structure = cls(data)
        
        start_time = time.time()
        for _ in range(num_searches):
            num = np.random.randint(0, size)
            structure.binary_search(num)
        end_time = time.time()
        
        avg_time = (end_time - start_time) / num_searches
        times.append(avg_time)
    
    return times

sizes = [1000, 2000, 4000, 8000]
linked_list_times = measure_performance(LinkedList, sizes)
array_times = measure_performance(Array, sizes)

plt.figure(figsize=(10, 6))
plt.plot(sizes, linked_list_times, label='Linked List', marker='o')
plt.plot(sizes, array_times, label='Array', marker='s')
plt.xlabel('Input Size')
plt.ylabel('Average Time (seconds)')
plt.title('Binary Search Performance: Linked List vs Array')
plt.legend()
plt.grid(True)
plt.show()
