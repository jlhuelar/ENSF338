import random
import timeit
import matplotlib.pyplot as plt
from timeit import Timer

class Node:
    def __init__(self, data, parent=None, left=None, right=None):
        self.parent = parent
        self.data = data
        self.left = left
        self.right = right

class BST:
    def __init__(self):
        self.root = None

    def insert(self, data):
        if self.root is None:
            self.root = Node(data)
        else:
            self._insert_recursive(data, self.root)

    def _insert_recursive(self, data, current):
        if data <= current.data:
            if current.left is None:
                current.left = Node(data, parent=current)
            else:
                self._insert_recursive(data, current.left)
        else:
            if current.right is None:
                current.right = Node(data, parent=current)
            else:
                self._insert_recursive(data, current.right)

    def search(self, data):
        return self._search_recursive(data, self.root)

    def _search_recursive(self, data, current):
        if current is None:
            return None
        elif data == current.data:
            return current
        elif data < current.data:
            return self._search_recursive(data, current.left)
        else:
            return self._search_recursive(data, current.right)

    def calculate_balance(self, node):
            if node is None:
                return 0
            left_height = self._height(node.left)
            right_height = self._height(node.right)
            return left_height - right_height

    def _height(self, node):
            if node is None:
                return -1
            return 1 + max(self._height(node.left), self._height(node.right))


def generate_tasks(n=1000):
    tasks = []
    base_list = list(range(1, n + 1))
    for _ in range(n):
        random.shuffle(base_list)
        tasks.append(list(base_list))
    return tasks

def perform_single_search_task(task):
    bst = BST()  # Create a new BST instance for this task
    for value in task:
        bst.insert(value)

    max_balance = 0
    for value in task:
        node = bst.search(value)
        balance = abs(bst.calculate_balance(node))
        if balance > max_balance:
            max_balance = balance
    return max_balance

def measure_performance(tasks):
    max_balances = []
    search_times = []

    for task in tasks:
        def task_execution():
            return perform_single_search_task(task)

        timer = Timer(task_execution)
        time_taken = timer.timeit(number=1)
        max_balance = task_execution()  # To get the max_balance after timing

        search_times.append(time_taken)
        max_balances.append(max_balance)

    return max_balances, search_times

def plot_results(max_balances, search_times):
    plt.scatter(max_balances, search_times)
    plt.title('Search Time vs. Largest Absolute Balance')
    plt.xlabel('Largest Absolute Balance')
    plt.ylabel('Search Time (seconds)')
    plt.show()

# Main execution
bst = BST()
tasks = generate_tasks()
max_balances, search_times = measure_performance(tasks)
plot_results(max_balances, search_times)