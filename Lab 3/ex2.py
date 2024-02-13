import random
import timeit
import matplotlib.pyplot as plt

def quicksort(arr):
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[0]
        less_than_pivot = [x for x in arr[1:] if x <= pivot]
        greater_than_pivot = [x for x in arr[1:] if x > pivot]
        return quicksort(less_than_pivot) + [pivot] + quicksort(greater_than_pivot)

def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

def generate_random_array(size):
    return [random.randint(1, 10000) for _ in range(size)]

sizes = [10, 40, 70, 100, 130, 160, 190, 220, 250, 280, 310, 340, 370, 400, 430, 460, 490, 520, 550, 580]
results = []

for size in sizes:
    array = generate_random_array(size)
    
    # Best Case for Bubble Sort (already sorted)
    bubble_best_time = timeit.timeit(lambda: bubble_sort(sorted(array)), number=10)
    
    # Worst Case for Bubble Sort (sorted in reverse order)
    bubble_worst_time = timeit.timeit(lambda: bubble_sort(sorted(array, reverse=True)), number=10)
    
    # Average Case for Bubble Sort
    bubble_avg_time = timeit.timeit(lambda: bubble_sort(array), number=10)
    
    # Best Case for Quicksort (already sorted)
    quick_best_time = timeit.timeit(lambda: quicksort(sorted(array)), number=10)
    
    # Worst Case for Quicksort (already sorted in reverse order)
    quick_worst_time = timeit.timeit(lambda: quicksort(sorted(array, reverse=True)), number=10)
    
    # Average Case for Quicksort
    quick_avg_time = timeit.timeit(lambda: quicksort(array), number=10)
    
    results.append((size, bubble_best_time, bubble_worst_time, bubble_avg_time, quick_best_time, quick_worst_time, quick_avg_time))

for size, bubble_best_time, bubble_worst_time, bubble_avg_time, quick_best_time, quick_worst_time, quick_avg_time in results:
    print(f"Size {size:>4}: Bubble Sort - Best: {bubble_best_time:.5f} seconds, Worst: {bubble_worst_time:.5f} seconds, Average: {bubble_avg_time:.5f} seconds")
    print(f"           Quicksort - Best: {quick_best_time:.5f} seconds, Worst: {quick_worst_time:.5f} seconds, Average: {quick_avg_time:.5f} seconds\n")
    
sizes = [result[0] for result in results]
bubble_best_times = [result[1] for result in results]
bubble_worst_times = [result[2] for result in results]
bubble_avg_times = [result[3] for result in results]
quick_best_times = [result[4] for result in results]
quick_worst_times = [result[5] for result in results]
quick_avg_times = [result[6] for result in results]

fig, axs = plt.subplots(3, 1, figsize=(10, 15))

# Plotting the performance for the best case scenario
axs[0].plot(sizes, bubble_best_times, label='Bubble Sort (Best)')
axs[0].plot(sizes, quick_best_times, label='Quicksort (Best)')

# Highlighting where one algorithm performs better than the other
for size, bubble_time, quick_time in zip(sizes, bubble_best_times, quick_best_times):
    if bubble_time < quick_time:
        axs[0].scatter(size, bubble_time, color='green')
    else:
        axs[0].scatter(size, quick_time, color='green')

axs[0].set_xlabel('Input Size')
axs[0].set_ylabel('Execution Time (seconds)')
axs[0].set_title('Best Case Scenario')
axs[0].legend()

# Plotting the performance for the worst case scenario
axs[1].plot(sizes, bubble_worst_times, label='Bubble Sort (Worst)')
axs[1].plot(sizes, quick_worst_times, label='Quicksort (Worst)')

# Highlighting where one algorithm performs better than the other
for size, bubble_time, quick_time in zip(sizes, bubble_worst_times, quick_worst_times):
    if bubble_time < quick_time:
        axs[1].scatter(size, bubble_time, color='green')
    else:
        axs[1].scatter(size, quick_time, color='green')

axs[1].set_xlabel('Input Size')
axs[1].set_ylabel('Execution Time (seconds)')
axs[1].set_title('Worst Case Scenario')
axs[1].legend()

# Plotting the performance for the average case scenario
axs[2].plot(sizes, bubble_avg_times, label='Bubble Sort (Average)')
axs[2].plot(sizes, quick_avg_times, label='Quicksort (Average)')

# Highlighting where one algorithm performs better than the other
for size, bubble_time, quick_time in zip(sizes, bubble_avg_times, quick_avg_times):
    if bubble_time < quick_time:
        axs[2].scatter(size, bubble_time, color='green')
    else:
        axs[2].scatter(size, quick_time, color='green')

axs[2].set_xlabel('Input Size')
axs[2].set_ylabel('Execution Time (seconds)')
axs[2].set_title('Average Case Scenario')
axs[2].legend()

plt.tight_layout()
plt.show()