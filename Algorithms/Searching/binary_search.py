# Suitable for sorted lists
# Repeatedly divide the search range to half until the target is found or cannot divide anymore
# Steps:
# 1. Start with the entire sorted list.
# 2. Compute the middle element of the list.
# 3. If the middle element is equal to the target value, return its index.
# 4. If the middle element is less than the target value, search in the right half of the list.
# 5. If the middle element is greater than the target value, search in the left half of the list.
# 6. Repeat steps 2-5 until the target value is found or the search interval is empty.


def binary_search(arr, target):
    """
    Perform binary search recursively to find the target value in the given sorted list.

    Parameters:
        arr (list): The sorted list to be searched.
        target: The value to be searched for.

    Returns:
        int: The index of the target value if found, otherwise -1.
    """
    low = 0
    high = len(arr) - 1
    while low <= high:
        mid = (low+high)//2
        if arr[mid] == target:
            return mid
        elif arr[mid] > target:
            high = mid - 1
        else:
            low = mid + 1
    
    return


# Example
arr = [2,3,10,22]
target = 4
result = binary_search(sorted(arr), target)
if result is not None:
    print(f"Element {target} found at index {result}.")
else:
    print(f"Cannot find element {target}.")
