# Steps:
# 1. Start with second element of the array as first element in the array is assumed to be sorted
# 2. Compare second element with the first element and check if the second element is smaller then swap them
# 3. Move to the third element and compare it with the first two elements and put at its correct position
# 4. Repeat until the entire array is sorted
# Time complexity: O(n) for best cases, O(n**2) for average and worst cases
# Space complexity: O(1)


def insertion_sort(arr: list):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = key

# Examples
arr = [12, 11, 13, 5, 6]
insertion_sort(arr)
print(arr)
