# 1. A profiler is a tool used to provide an execution profile for a given program, meaning it gives a profile of statistics to describe 
#    and measure relative system statistics and behaviours such as long and how often various of parts of a program are executed
# 2. Profiling differs from benchmarking because in profiling you measure the relative system performance and with benchmarking,
#    you measure the absolute system performance through different hardware, compliers, and other systems to test the performance.
# 3. 7.203 seconds
# 4. A sample output for profiling a program would include column headings that describes different statistics. This includes
#    how many function calls were monitored(ncalls), total time spent in function(tottime), average time per call to its functions (percall). 
#    cumulative time spent in function(cumtime) and how the data and functions are sorted in the profile(Ordered by: ).
#    The execution time is the first line that is given when a profile is created, it recognizes how many function calls were made in the execution time.

import profile
import timeit
def sub_function(n):
    #sub function that calculates the factorial of n
    if n == 0:
        return 1
    else:
        return n * sub_function(n-1)
    
def test_function():
    data = []
    for i in range(10):
        data.append(sub_function(i))
    return data

def third_function():
    # third function that calculates the square of the numbers from 0 to 999
    return [i**2 for i in range(100000000)]

test_function()
third_function()

if __name__ == "__main__":
    # Create a Profile object
    profiler = profile.Profile()
    # Run the profiler on the code within the if __name__ block
    profiler.run("test_function(); third_function()")
    # Print the profiling results
    profiler.print_stats()