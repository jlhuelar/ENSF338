


import json

with open('ex7data.json', 'r') as file:
    data = json.load(file)


array = 
numbers_array = data['numbers']
first = 0
last = len(arr) - 1
key = int(input("Enter the value you are searching for: "))
custom_mid_input = input(f"Enter a custom midpoint index (between 0 and {len(arr) - 1}): ")

def binarySearch(arr, first, last, key, customMid=None, isFirstIteration=True):
    if first <= last:
        if isFirstIteration and customMid is not None:
            mid = customMid
        else:
            mid = (first + last) // 2  # Standard way to find the midpoint
        
        if key == arr[mid]:
            return mid  # success: key found
        elif key < arr[mid]:
            return binarySearch(arr, first, mid - 1, key, None, False)  # No need for customMid now
        else:
            return binarySearch(arr, mid + 1, last, key, None, False)  # No need for customMid now
    return -1  # failure: key not found