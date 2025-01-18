# Steps:
# 1. Find the smallest element and swap it with the first element. This way we get the smallest element at its correct position.
# 2. Find the smallest among remaining elements (or second smallest) and swap it with the second element.
# 3. Keep doing this until we get all elements moved to correct position.
# Time complexity:  O(n**2)
# Space complexity: O(1)

def selection_sort(arr):
    n = len(arr)
    for i in range(len(arr)-1):
        min_index = i
        for j in range(i+1, len(arr)):
            if arr[min_index] > arr[j]:
                min_index = j

        arr[i], arr[min_index] = arr[min_index], arr[i]


# Examples
arr = [64, 25, 12, 22, 11]
selection_sort(arr)
print(arr)
