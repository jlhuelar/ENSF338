class CircularQueueArray:
    def __init__(self, capacity):
        self.capacity = capacity
        self.queue = [None] * capacity
        self.front = 0
        self.rear = 0
        self.size = 0

    def enqueue(self, item):
        if self.size == self.capacity:
            print("enqueue None")
            return
        self.queue[self.rear] = item
        self.rear = (self.rear + 1) % self.capacity
        self.size += 1
        print(f"enqueue {item}")

    def dequeue(self):
        if self.size == 0:
            print("dequeue None")
            return None
        item = self.queue[self.front]
        self.queue[self.front] = None
        self.front = (self.front + 1) % self.capacity
        self.size -= 1
        print(f"dequeue {item}")
        return item

    def peek(self):
        if self.size == 0:
            print("peek None")
            return None
        item = self.queue[self.front]
        print(f"peek {item}")
        return item

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class CircularQueueLinkedList:
    def __init__(self):
        self.front = None
        self.rear = None

    def enqueue(self, item):
        if self.is_full():
            print("enqueue None")
            return
        new_node = Node(item)
        if self.is_empty():
            self.front = new_node
        else:
            self.rear.next = new_node
        self.rear = new_node
        print(f"enqueue {item}")

    def dequeue(self):
        if self.is_empty():
            print("dequeue None")
            return None
        item = self.front.data
        self.front = self.front.next
        if self.front is None:
            self.rear = None
        print(f"dequeue {item}")
        return item

    def peek(self):
        if self.is_empty():
            print("peek None")
            return None
        item = self.front.data
        print(f"peek {item}")
        return item

    def is_empty(self):
        return self.front is None

    def is_full(self):
        # For a linked list, it's not limited by capacity.
        return False

# Generate list of 40 operations for testing
operations = [
    ("enqueue", 1),     # enqueue 1
    ("peek", 1),        # peek 1
    ("dequeue", 1),     # dequeue 1
    ("enqueue", 2),     # enqueue 2
    ("enqueue", 3),     # enqueue 3
    ("enqueue", 4),     # enqueue 4
    ("enqueue", 5),     # enqueue 5
    ("dequeue", 2),     # dequeue 2
    ("dequeue", 3),     # dequeue 3
    ("dequeue", 4),     # dequeue 4
    ("peek", 5),        # peek 5
    ("enqueue", None),  # enqueue None
    ("dequeue", None),  # dequeue None
    ("peek", None),     # peek None
    ("enqueue", 6),     # enqueue 6
    ("enqueue", 7),     # enqueue 7
    ("enqueue", 8),     # enqueue 8
    ("enqueue", 9),     # enqueue 9
    ("enqueue", 10),    # enqueue 10
    ("peek", 6),        # peek 6
    ("dequeue", 6),     # dequeue 6
    ("dequeue", 7),     # dequeue 7
    ("dequeue", 8),     # dequeue 8
    ("dequeue", 9),     # dequeue 9
    ("peek", 10),       # peek 10
    ("enqueue", None),  # enqueue None
    ("dequeue", None),  # dequeue None
    ("peek", None),     # peek None
    ("enqueue", 11),    # enqueue 11
    ("enqueue", 12),    # enqueue 12
    ("enqueue", 13),    # enqueue 13
    ("enqueue", 14),    # enqueue 14
    ("enqueue", 15),    # enqueue 15
    ("dequeue", 11),    # dequeue 11
    ("dequeue", 12),    # dequeue 12
    ("dequeue", 13),    # dequeue 13
    ("peek", 14),       # peek 14
    ("enqueue", 16),    # enqueue 16
    ("enqueue", 17)     # enqueue 17
]

# Function to perform operations on a queue
def test_queue(queue, operations):
    for operation, item in operations:
        if operation == "enqueue":
            queue.enqueue(item)
        elif operation == "dequeue":
            queue.dequeue()
        elif operation == "peek":
            queue.peek()

# Perform operations on CircularQueueArray
print("Testing CircularQueueArray:")
queue_array = CircularQueueArray(5)
test_queue(queue_array, operations)

# Perform operations on CircularQueueLinkedList
print("\nTesting CircularQueueLinkedList:")
queue_linked_list = CircularQueueLinkedList()
test_queue(queue_linked_list, operations)
