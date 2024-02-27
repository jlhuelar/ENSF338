class PriorityQueueMergeSort:
    def __init__(self):
        self.queue = []
    
    def merge_sort(self, array):
        if len(array) > 1:
            mid = len(array) // 2
            left_half = array[:mid]
            right_half = array[mid:]

            self.merge_sort(left_half)
            self.merge_sort(right_half)

            i = j = k = 0

            while i < len(left_half) and j < len(right_half):
                if left_half[i] < right_half[j]:
                    array[k] = left_half[i]
                    i += 1
                else:
                    array[k] = right_half[j]
                    j += 1
                k += 1

            while i < len(left_half):
                array[k] = left_half[i]
                i += 1
                k += 1

            while j < len(right_half):
                array[k] = right_half[j]
                j += 1
                k += 1
    
    def enqueue(self, item):
        self.queue.append(item)
        self.merge_sort(self.queue)
    
    def dequeue(self):
        if len(self.queue) == 0:
            return None
        return self.queue.pop(0)

    def peek(self):
        if len(self.queue) == 0:
            return None
        return self.queue[0]

    def is_empty(self):
        return len(self.queue) == 0

    def size(self):
        return len(self.queue)

class PriorityQueueSortedInsert:
    def __init__(self):
        self.queue = []
    
    def enqueue(self, item):
        if len(self.queue) == 0:
            self.queue.append(item)
        else:
            inserted = False
            for i in range(len(self.queue)):
                if item < self.queue[i]:
                    self.queue.insert(i, item)
                    inserted = True
                    break
            if not inserted:
                self.queue.append(item)
    
    def dequeue(self):
        if len(self.queue) == 0:
            return None
        return self.queue.pop(0)

    def peek(self):
        if len(self.queue) == 0:
            return None
        return self.queue[0]

    def is_empty(self):
        return len(self.queue) == 0

    def size(self):
        return len(self.queue)

import random
import timeit

def generate_task_list(num_tasks=1000):
    tasks = []
    for _ in range(num_tasks):
        # Generate a random number between 0 and 1
        operation = random.random()
        # If the number is less than 0.7, the operation is 'enqueue', otherwise 'dequeue'
        if operation < 0.7:
            # For 'enqueue', generate a random integer to enqueue
            tasks.append(('enqueue', random.randint(1, 100)))
        else:
            tasks.append(('dequeue', None))
    return tasks

# Function to process a list of tasks using a given priority queue
def process_tasks(task_list, queue):
    for task in task_list:
        operation, value = task
        if operation == 'enqueue':
            queue.enqueue(value)
        elif operation == 'dequeue':
            queue.dequeue()

# Function to measure the performance of a priority queue implementation
def measure_performance(queue_class):
    total_time = 0
    # Repeat the measurement for 100 lists
    for _ in range(100):
        task_list = generate_task_list()
        queue = queue_class()
        # Measure the time taken to process the task list
        time_taken = timeit.timeit(lambda: process_tasks(task_list, queue), number=1)
        total_time += time_taken
    return total_time / 100  # Return the average time

# Measure performance of both priority queue implementations
avg_time_merge_sort = measure_performance(PriorityQueueMergeSort)
avg_time_sorted_insert = measure_performance(PriorityQueueSortedInsert)

print(f"Average time for PriorityQueueMergeSort: {avg_time_merge_sort} seconds")
print(f"Average time for PriorityQueueSortedInsert: {avg_time_sorted_insert} seconds")

# 5. Given the probability distribution of enqueue and dequeue and the overhead of sorting in 'PriorityQueueMergeSort', we would
#    expect the 'PriorityQueueSortedInsert' to be faster on average. This is true as the average time for 'PriorityQueueSortedInsert'
#    is much faster than the average time for 'PriorityQueueMergeSort' when their performance is measured. This is because inserting 
#    in the correct position is more efficient than sorting the entire array after each enqueue, especially as the number of 
#    elements increases.
