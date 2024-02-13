# 1. The strategy used to grow arrays in the lists.c code is designed to balance between memory efficiency and performance, particularly
#    to accomodate additional growth without frequent reallocations. This is achieved through and over-allocation mechanism. The function
#    'list_resize' first checks if the current allocation ('allocated') is sufficient for the new size ('newsize'). When the list needs
#    to grow, the new allocated size is calculated using a growth factor. Ths code uses the formula 'new_allocated = ((size_t)newsize + 
#    (newsize >> 3) + 6) & ~(size_t)3;'. The code also includes a condition to prevent over-allocation. The new memory allocation is
#    then performed based on the calculated 'new_allocated' size. The specific choice of growth factor and the additional padding are
#    optimizations tailored to balance between using memory efficiently and minimizing the overhead of reallocations.

import sys
import timeit
import matplotlib.pyplot as plt

# Checking for capacity changes
prev_size = 0
for i in range(64):
    lst = [0] * i
    current_size = sys.getsizeof(lst)
    if current_size != prev_size:
        print(f"Capacity changed at {i} elements, size in bytes: {current_size}")
        prev_size = current_size


# Measuring time for growing array from S to S+1 and S-1 to S
# Assuming the last capacity change before 64 is significant for S
S = 63

def grow_from_S_to_S_plus_1():
    lst = [0] * S
    lst.append(1)

def grow_from_S_minus_1_to_S():
    lst = [0] * (S - 1)
    lst.append(1)

time_S_to_S_plus_1 = timeit.repeat(grow_from_S_to_S_plus_1, number=1, repeat=1000)
time_S_minus_1_to_S = timeit.repeat(grow_from_S_minus_1_to_S, number=1, repeat=1000)

# Plotting the distributions
plt.figure(figsize=(12, 6))

plt.hist(time_S_to_S_plus_1, bins=30, alpha=0.5, label='Grow from S to S+1')
plt.hist(time_S_minus_1_to_S, bins=30, alpha=0.5, label='Grow from S-1 to S')
plt.xlabel('Time (seconds)')
plt.ylabel('Frequency')
plt.legend()
plt.title('Time Distribution for Growing List Size')
plt.show()
