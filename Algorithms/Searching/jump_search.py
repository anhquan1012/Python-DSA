# Used for sorted lists
# Jump ahead by a fixed number of steps. Then performs linear search on smaller range
# Steps:
# 1. Determine the block size to jump ahead.
# 2. Jump ahead by block size until the target value is greater than the current block's last element.
# 3. Perform linear search within the current block to find the target value.
# 4. If the target value is found, return its index.
# 5. If the target value is not found after iterating through all blocks, return -1.


import math
import random


def jump_search(arr, target):
    """
    Perform jump search to find the target value in the given sorted list.

    Parameters:
        arr (list): The sorted list to be searched.
        target: The value to be searched for.

    Returns:
        int: The index of the target value if found, otherwise -1.
    """
    n = len(arr)
    step = int(math.sqrt(n))
    prev = 0
    while arr[min(step, n) - 1] < target:
        prev = step
        step += int(math.sqrt(n))
        if prev >= n:
            return -1
    while arr[prev] < target:
        prev += 1
        if prev == min(step, n):
            return -1
    if arr[prev] == target:
        return prev
    return 


# Example
arr = random.sample(range(1, 100), 50)
target = random.randint(1, 100)
print(f"Arr: {sorted(arr)}")
print(f"Target: {target}")
result = jump_search(sorted(arr), target)
if result is not None:
    print(f"Element {target} found at index {result}.")
else:
    print(f"Cannot find element {target}.")