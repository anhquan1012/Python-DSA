def linear_search(arr, target):
    """
    Perform linear search to find the target value in the given list.

    Parameters:
        arr (list): The list to be searched.
        target: The value to be searched for.

    Returns:
        int: The index of the target value if found, otherwise -1.
    """
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return


# Example
arr = [1,3,10,22,88,999]
target = 2
result = linear_search(arr, target)
if result is not None:
    print(f"Element {target} found at index {result}.")
else:
    print(f"Cannot find element {target}.")
