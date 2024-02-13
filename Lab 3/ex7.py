#   4. The initial midpoint appears to affect performance because based on binary search, a divide and conquer alghoritim,
#      choosing a midpoint closer to the target value or search task, will result in lesser computations to get to that value.
#      Less time to get to that search task based on effective initial midpoint will result in faster to divide and conquer
#      to search if that value is present or not

import json
import timeit
import matplotlib.pyplot as plt

def load_large_array(file_path):
    with open(file_path, 'r') as file:
        return json.load(file)

def binary_search(array, target, start_mid=None):
    low, high = 0, len(array) - 1
    mid = start_mid if start_mid is not None else (low + high) // 2

    while low <= high:
        if array[mid] == target:
            return True
        elif array[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
        
        # For subsequent iterations, calculate mid normally
        mid = (low + high) // 2
    
    return False

def load_search_tasks(file_path):
    with open(file_path, 'r') as file:
        return json.load(file)

large_array_file = 'ex7data.json'
search_tasks_file = 'ex7tasks.json'
large_array = load_large_array(large_array_file)
search_tasks = load_search_tasks(search_tasks_file)

def perform_search_tasks(large_array_file, search_tasks_file):
    large_array = load_large_array(large_array_file)
    search_tasks = load_search_tasks(search_tasks_file)
    results = {}

    start_mid = int(input("Enter the starting midpoint index: "))

    for task in search_tasks:
        results[task] = binary_search(large_array, task, start_mid)

    return results

def time_search_with_midpoints(array, target, midpoints):
    results = {}
    for mid in midpoints:
        timer = timeit.timeit(lambda: binary_search(array, target, mid), number=10)
        results[mid] = timer
    return results

def find_best_midpoints_for_tasks(large_array, search_tasks):
    best_midpoints = {}
    midpoints = [len(large_array) // 4, len(large_array) // 2, 3 * len(large_array) // 4]  # Example strategies

    for task in search_tasks:
        timings = time_search_with_midpoints(large_array, task, midpoints)
        best_mid = min(timings, key=timings.get)  # Find the midpoint with the best (lowest) time
        best_midpoints[task] = best_mid

        print(f"Timings for Task {task}: {timings}")

    return best_midpoints

best_midpoints = find_best_midpoints_for_tasks(large_array, search_tasks)

for task, mid in best_midpoints.items():
    print(f"Best midpoint for {task}: {mid}")

results = perform_search_tasks(large_array_file, search_tasks_file)

for task in search_tasks:
    found = binary_search(large_array, task, best_midpoints[task])
    print(f"Number {task} is {'found' if found else 'not found'} in the array.")

tasks = sorted(list(best_midpoints.keys()))  
provided_midpoints = [best_midpoints[task] for task in tasks]

plt.figure(figsize=(10, 6))
plt.scatter(tasks, provided_midpoints, color='blue', alpha=0.5)  
plt.title('Chosen Midpoint for Each Task')
plt.xlabel('Tasks')
plt.ylabel('Chosen Midpoint')
plt.xticks(tasks)
plt.show()