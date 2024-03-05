class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class ListPriorityQueue:
    def __init__(self):
        self.head = None
    
    def enqueue(self, value):
        new_node = Node(value)
        if self.head is None or self.head.value >= value:
            new_node.next = self.head
            self.head = new_node
        else:
            current = self.head
            while current.next and current.next.value < value:
                current = current.next
            new_node.next = current.next
            current.next = new_node

    def dequeue(self):
        if self.head is None:
            return None
        value = self.head.value
        self.head = self.head.next
        return value

import heapq

class HeapPriorityQueue:
    def __init__(self):
        self.heap = []
    
    def enqueue(self, value):
        heapq.heappush(self.heap, value)
    
    def dequeue(self):
        if self.heap:
            return heapq.heappop(self.heap)
        return None

import random
import timeit

# Function to generate a random list of tasks
def generate_tasks(n=1000, enqueue_prob=0.7):
    tasks = []
    for _ in range(n):
        if random.random() < enqueue_prob:
            tasks.append(('enqueue', random.randint(0, 1000)))
        else:
            tasks.append(('dequeue', None))
    return tasks

# Function to process tasks with a given priority queue
def process_tasks(pq_class, tasks):
    pq = pq_class()
    for op, value in tasks:
        if op == 'enqueue':
            pq.enqueue(value)
        elif op == 'dequeue':
            pq.dequeue()

# Generate a random list of 1000 tasks
tasks = generate_tasks()

# Measure execution time for ListPriorityQueue
list_pq_time = timeit.timeit('process_tasks(ListPriorityQueue, tasks)', globals=globals(), number=1)

# Measure execution time for HeapPriorityQueue
heap_pq_time = timeit.timeit('process_tasks(HeapPriorityQueue, tasks)', globals=globals(), number=1)

print(f"ListPriorityQueue total time: {list_pq_time} seconds")
print(f"ListPriorityQueue average time per task: {list_pq_time / 1000} seconds")
print(f"HeapPriorityQueue total time: {heap_pq_time} seconds")
print(f"HeapPriorityQueue average time per task: {heap_pq_time / 1000} seconds")

# 4. The 'HeapPriorityQueue' was found to be faster in the execution of the above code, indicating that the heap-based implementation
#    offered advantages in efficiency over the linked list implementation under the conditions tested. One reason for this could be
#    that heaps are very efficient at maintaining their structure when elements are added or removed, which is essential for
#    priority queues where the order of elements is crucial. The heap can insert a new element or remove the smallest element in
#    O(logn) time, where n is the number of elements in the heap. This efficiency can become significant as the number of elements
#    increases. Given this outcome, it suggests that for the task distribution and data sizes involved in this implementation, the
#    heap-based priority queue is more efficient.