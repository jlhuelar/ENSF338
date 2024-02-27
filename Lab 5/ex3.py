import random
import timeit
import matplotlib.pyplot as plt

class ArrayStack:
    def __init__(self):
        self.stack = []

    def push(self, item):
        self.stack.append(item)

    def pop(self):
        if not self.is_empty():
            return self.stack.pop()
        else:
            raise IndexError("pop from an empty stack")

    def is_empty(self):
        return len(self.stack) == 0

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedListStack:
    def __init__(self):
        self.head = Node("head")
        self.size = 0

    def is_empty(self):
        return self.size == 0
    
    def push(self, value):
        node = Node(value)
        node.next = self.head.next
        self.head.next = node
        self.size += 1

    def pop(self):
        if self.is_empty():
            raise IndexError("pop from an empty stack")
        remove = self.head.next
        self.head.next = self.head.next.next
        self.size -= 1
        return remove.value

def generate_random_task_list(num_tasks=10000):
    tasks = []
    probability = random.random()
    for _ in range(num_tasks):
        if probability > 0.3:
            tasks.append('push')
        else:
            tasks.append('pop') 
    return tasks

def perform_tasks(stack, tasks):
    for task in tasks:
        if task == 'push':
            stack.push(1)
        elif task == 'pop':
            try:
                stack.pop()
            except IndexError:
                pass

array_stack_times = []
linked_list_stack_times = []

for _ in range(100):
    array_stack = ArrayStack()
    linked_list_stack = LinkedListStack()
    tasks = generate_random_task_list()

    array_stack_time = timeit.timeit(lambda: perform_tasks(array_stack, tasks), number=1)
    linked_list_stack_time = timeit.timeit(lambda: perform_tasks(linked_list_stack, tasks), number=1)

    array_stack_times.append(array_stack_time)
    linked_list_stack_times.append(linked_list_stack_time)

print("Average time taken by ArrayStack:", sum(array_stack_times) / len(array_stack_times))
print("Average time taken by LinkedListStack:", sum(linked_list_stack_times) / len(linked_list_stack_times))

plt.hist(array_stack_times, bins=10, alpha=0.5, label='ArrayStack')
plt.hist(linked_list_stack_times, bins=10, alpha=0.5, label='LinkedListStack')
plt.legend(loc='upper right')
plt.xlabel('Time (s)')
plt.ylabel('Frequency')
plt.title('Distribution of Execution Times')
plt.show()