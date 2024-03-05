import random

class MinHeap:
    def __init__(self):
        self.heap = []

    def heapify(self, arr):
        self.heap = arr
        for i in range((len(self.heap) // 2) - 1, -1, -1):
            self._sift_down(i)

    def enqueue(self, element):
        self.heap.append(element)
        self._sift_up(len(self.heap) - 1)

    def dequeue(self):
        if len(self.heap) == 0:
            return None
        self._swap(0, len(self.heap) - 1)
        min_element = self.heap.pop()
        self._sift_down(0)
        return min_element

    def _sift_up(self, index):
        parent_index = (index - 1) // 2
        if parent_index >= 0 and self.heap[parent_index] > self.heap[index]:
            self._swap(index, parent_index)
            self._sift_up(parent_index)

    def _sift_down(self, index):
        smallest = index
        left_child = 2 * index + 1
        right_child = 2 * index + 2

        if left_child < len(self.heap) and self.heap[left_child] < self.heap[smallest]:
            smallest = left_child

        if right_child < len(self.heap) and self.heap[right_child] < self.heap[smallest]:
            smallest = right_child

        if smallest != index:
            self._swap(index, smallest)
            self._sift_down(smallest)

    def _swap(self, i, j):
        self.heap[i], self.heap[j] = self.heap[j], self.heap[i]

def test_heapify_already_heap():
    min_heap = MinHeap()
    input_array = [1, 2, 3, 4, 5, 6]
    min_heap.heapify(input_array)
    if min_heap.heap == input_array:
        print("Test heapify with already heap: Passed")
    else:
        print("Test heapify with already heap: Failed")

def test_heapify_empty_array():
    min_heap = MinHeap()
    input_array = []
    min_heap.heapify(input_array)
    if min_heap.heap == []:
        print("Test heapify with empty array: Passed")
    else:
        print("Test heapify with empty array: Failed")

def test_heapify_random_shuffled_array():
    min_heap = MinHeap()
    input_array = [i for i in range(1, 101)]  
    random.shuffle(input_array) 
    min_heap.heapify(input_array)
    if min_heap.heap[0] == min(input_array):
        print("Test heapify with random shuffled array: Passed")
    else:
        print("Test heapify with random shuffled array: Failed")

test_heapify_already_heap()
test_heapify_empty_array()
test_heapify_random_shuffled_array()

