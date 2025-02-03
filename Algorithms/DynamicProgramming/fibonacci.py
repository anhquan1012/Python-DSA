# Dynamic Programming is an algorithmic technique with the following properties.
# 1. It is mainly an optimization over plain recursion. Wherever we see a recursive solution that has repeated calls for the same inputs, we can optimize it using Dynamic Programming.
# 2. The idea is to simply store the results of subproblems so that we do not have to re-compute them when needed later. This simple optimization typically reduces time complexities from exponential to polynomial.


def fibonacci(n):
    if n < 2:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)
    

cache = {}
def dynamic_fibonacci(n):
    if n in cache:
        return cache[n]
    elif n < 2:
        return n
    else:
        cache[n] = dynamic_fibonacci(n-1) + dynamic_fibonacci(n-2)
        return cache[n]


# Examples
import time

print(fibonacci(5))

start = time.time()
print(fibonacci(40))
print(time.time() - start)

start2 = time.time()
print(dynamic_fibonacci(40))
print(time.time() - start2)

