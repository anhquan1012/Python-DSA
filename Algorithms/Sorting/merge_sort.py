# Merge sort follows the divide-and-conquer approach. 
# It works by recursively dividing the input array into smaller subarrays and sorting those subarrays then merging them back together to obtain the sorted array.
# Steps:
# 1. Divide: Divide the list or array recursively into two halves until it can no more be divided.
# 2. Conquer: Each subarray is sorted individually using the merge sort algorithm.
# 3. Merge: The sorted subarrays are merged back together in sorted order. The process continues until all elements from both subarrays have been merged.
# Time complexity: O(n*logn)
# Space complexity: O(n)


def merge_sort(arr: list):
    if len(arr) == 1:
        return arr
    else:
        # Divide
        mid = len(arr) // 2
        left_arr = arr[:mid]
        right_arr = arr[mid:]

        return merge(merge_sort(left_arr), merge_sort(right_arr))

def merge(left_arr, right_arr):
    left = len(left_arr)
    right = len(right_arr)

    l = 0
    r = 0
    sorted_arr = []
    while l < left and r < right:
        if left_arr[l] < right_arr[r]:
            sorted_arr.append(left_arr[l])
            l += 1
        else:
            sorted_arr.append(right_arr[r])
            r += 1

    return sorted_arr + left_arr[l:] + right_arr[r:]


# Examples
arr = [12, 11, 13, 5, 6, 7]
sorted_arr = merge_sort(arr)
print(sorted_arr)
