#   4. Worst-case complexity is O(n) for linear search when the element searched is the last element in an array
#      Worst-case is O(log n) for binary search when the element searched is the first, last or does not exist in an array

import timeit
import matplotlib as py


#Inefficient Implementation
def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1  

#Efficient Implementation
def binary_search(arr, target):
    left = 0
    right = len(arr) - 1

    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return -1  