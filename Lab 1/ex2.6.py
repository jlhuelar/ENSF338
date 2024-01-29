import timeit

def pow2(n):
    return 2 ** n

n = 10

result = pow2(n)
print(result)

execution_time = timeit.timeit(lambda: pow2(10000), number=10000)
print("Time it takes to execute 10000 instances of pow2(10000):", execution_time)

