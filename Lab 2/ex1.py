# 1. This code defines a recursive function 'func' that calculates the 'n'-th number in the Fibonacci sequence.
# 2. This does not fully represent a divide-and-conquer algorithm. While the Fibonacci function is recursive and does break it down 
#    into smaller pieces ('func(n-1)' and 'func(n-2)'), there is no complexity in solving these subproblems other than applying
#    the same function over again. There is no direct "conquer" phase and it's "combine" step is quite simple. Additionally, the size
#    of its subproblems are unequal.
# 3. An expression for its time complexity is O(2^n) due to its exponential growth in the number of function calls.

def fibonacci_memo(n, memo=None):
    if memo is None:
        memo = {}
    if n in memo:
        return memo[n]
    if n == 0 or n == 1:
        return n
    else:
        result = fibonacci_memo(n - 1, memo) + fibonacci_memo(n - 2, memo)
        memo[n] = result
        return result

# 5. The time complexity of the optimized algoritm is O(n).
    
import time
import matplotlib.pyplot as plt

def fibonacci_recursive(n):
    if n == 0 or n == 1:
        return n
    else:
        return fibonacci_recursive(n-1) + fibonacci_recursive(n-2)

def fibonacci_memo(n, memo=None):
    if memo is None:
        memo = {}
    if n in memo:
        return memo[n]
    if n == 0 or n == 1:
        return n
    else:
        result = fibonacci_memo(n - 1, memo) + fibonacci_memo(n - 2, memo)
        memo[n] = result
        return result
    
def time_fibonacci_functions(max_n):
    times_recursive = []
    times_memoized = []

    for n in range(max_n +1 ):
        start_time = time.time()
        fibonacci_recursive(n)
        end_time = time.time()
        times_recursive.append(end_time - start_time)

        start_time = time.time()
        fibonacci_memo(n)
        end_time = time.time()
        times_memoized.append(end_time - start_time)

    return times_recursive, times_memoized

max_n = 35

times_recursive, times_memoized = time_fibonacci_functions(max_n)

plt.figure(figsize=(10, 6))
plt.plot(range(max_n + 1), times_recursive, marker='o', color='red', label='Recursive')
plt.title('Execution Time of Recursive Fibonacci Function')
plt.xlabel('n')
plt.ylabel('Time (seconds)')
plt.grid(True)
plt.legend()
plt.savefig('Lab 2/ex1.6.1.jpg')

plt.figure(figsize=(10, 6))
plt.plot(range(max_n + 1), times_memoized, marker='o', color='blue', label='Memoized')
plt.title('Execution Time of Memoized Fibonacci Function')
plt.xlabel('n')
plt.ylabel('Time (seconds)')
plt.grid(True)
plt.legend()
plt.savefig('Lab 2/ex1.6.2.jpg')