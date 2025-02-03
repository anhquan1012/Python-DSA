# Recursion involves a function calling itself directly or indirectly to solve a problem by breaking it down into simpler and more manageable parts
# Base Case: This is the condition under which the recursion stops. It is crucial to prevent infinite loops and to ensure that each recursive call reduces the problem in some manner
# Recursive Case: This is the part of the function that includes the call to itself. It must eventually lead to the base case


def iterative_factorial(number):
    f = 1
    for i in range(1, number+1):
        f = f * i
    return f

print(iterative_factorial(0))
#1
print(iterative_factorial(5))
#120
print(iterative_factorial(50))
#30414093201713378043612608166064768844377641568960512000000000000

def recursive_factorial(number):
    if number <= 1:
        return 1
    else:
        return number * recursive_factorial(number-1)
    
print(recursive_factorial(0))
#1
print(recursive_factorial(5))
#120
print(recursive_factorial(50))
#30414093201713378043612608166064768844377641568960512000000000000
