# Steps:
# 1. Outer loop: iterate through the list multiple times, reduce the range of comparison after each pass
# 2. Inner loop: for each element, compare with next elemen => Swap if current element is greater than the next one
# 3. Continue to the end of loop
# Time complexity: O(n**2)
# Space complexity: O(1)


def bubble_sort(arr: list):
    for i in range(len(arr)):
        swapped = False
        for j in range(len(arr)-i-1):
            if arr[j] > arr[j+1]:
                tmp = arr[j]
                arr[j] = arr[j+1]
                arr[j+1] = tmp
                swapped = True
        
        # Stop because the list is sorted
        if not swapped:
            break


# Examples
arr = [64, 34, 25, 12, 22, 11, 90]
bubble_sort(arr)
print(arr)