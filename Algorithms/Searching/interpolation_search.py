# Interpolation search is an improved version of binary search, especially suitable for large and uniformly distributed arrays. 
# Calculate the probable position of the target value based on the value of the key and the range of the search space.
# Steps:
# 1. Calculate the probable position of the target value using interpolation formula.
# 2. Compare the target value with the element at the calculated position.
# 3. If the element matches the target value, return its index.
# 4. If the element is less than the target value, search in the right half of the list.
# 5. If the element is greater than the target value, search in the left half of the list.
# 6. Repeat steps 1-5 until the target value is found or the search interval is empty.


import random


def interpolation_search(arr, target):
    """
    Perform interpolation search to find the target value in the given sorted list.

    Parameters:
        arr (list): The sorted list to be searched.
        target: The value to be searched for.

    Returns:
        int: The index of the target value if found, otherwise -1.
    """
    low = 0
    high = len(arr) - 1
    while low <= high and target >= arr[low] and target <= arr[high]:
        pos = low + ((high - low) // (arr[high] - arr[low])) * (target - arr[low])
        if arr[pos] == target:
            return pos
        elif arr[pos] < target:
            low = pos + 1
        else:
            high = pos - 1
    return


# Example
arr = random.sample(range(1, 100), 50)
target = random.randint(1, 100)
print(f"Arr: {sorted(arr)}")
print(f"Target: {target}")
result = interpolation_search(sorted(arr), target)
if result is not None:
    print(f"Element {target} found at index {result}.")
else:
    print(f"Cannot find element {target}.")
