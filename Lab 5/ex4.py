import random
import timeit
import matplotlib.pyplot as plt
import numpy as np

# Implementations of the two queue types
class ArrayQueue:
    def __init__(self):
        self.queue = []
    
    def enqueue(self, item):
        self.queue.insert(0, item)
    
    def dequeue(self):
        if len(self.queue) == 0:
            return None
        return self.queue.pop()

class Node:
    def __init__(self, value=None):
        self.value = value
        self.next = None

class LinkedListQueue:
    def __init__(self):
        self.head = None
        self.tail = None
    
    def enqueue(self, item):
        new_node = Node(item)
        if self.tail:
            self.tail.next = new_node
        self.tail = new_node
        if not self.head:
            self.head = new_node
    
    def dequeue(self):
        if not self.head:
            return None
        removed_value = self.head.value
        self.head = self.head.next
        if self.head is None:
            self.tail = None
        return removed_value

# Function to generate random task lists
def generate_task_list(num_tasks=10000):
    return [('enqueue', random.randint(1, 100)) if random.random() < 0.7 else ('dequeue', None) for _ in range(num_tasks)]

# Function to process a list of tasks on a given queue
def process_tasks(task_list, queue):
    for task in task_list:
        operation, item = task
        if operation == 'enqueue':
            queue.enqueue(item)
        elif operation == 'dequeue':
            queue.dequeue()

# Function to measure the performance of processing a single list of tasks for a given queue implementation
def measure_single_list_performance(queue_class, task_list):
    queue = queue_class()
    start_time = timeit.default_timer()
    process_tasks(task_list, queue)
    return timeit.default_timer() - start_time

# Generating 100 random task lists
task_lists = [generate_task_list() for _ in range(100)]

# Measuring performance for both queue implementations
times_array_queue = [measure_single_list_performance(ArrayQueue, task_list) for task_list in task_lists]
times_linked_list_queue = [measure_single_list_performance(LinkedListQueue, task_list) for task_list in task_lists]

# Plotting the distributions with annotations for mean and standard deviation
plt.figure(figsize=(12, 8))
plt.hist(times_array_queue, bins=20, alpha=0.5, label='ArrayQueue', color='blue')
plt.hist(times_linked_list_queue, bins=20, alpha=0.5, label='LinkedListQueue', color='green')

mean_array_queue, std_array_queue = np.mean(times_array_queue), np.std(times_array_queue)
mean_linked_list_queue, std_linked_list_queue = np.mean(times_linked_list_queue), np.std(times_linked_list_queue)

plt.axvline(mean_array_queue, color='blue', linestyle='dashed', linewidth=1)
plt.text(mean_array_queue, plt.ylim()[1]*0.9, f'Mean: {mean_array_queue:.2f}\nStd: {std_array_queue:.2f}', color='blue')

plt.axvline(mean_linked_list_queue, color='green', linestyle='dashed', linewidth=1)
plt.text(mean_linked_list_queue, plt.ylim()[1]*0.7, f'Mean: {mean_linked_list_queue:.2f}\nStd: {std_linked_list_queue:.2f}', color='green')

plt.xlabel('Time (seconds)')
plt.ylabel('Frequency')
plt.title('Performance Distribution of Queue Implementations')
plt.legend()
plt.grid(True)
plt.show()
