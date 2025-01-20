# Steps:
# 1. Heapify: rearrange array elements so that they form a Max Heap
# 2. Swap the root element of the heap (which is the largest element in current heap) with the last element of the heap
# 3. Remove the last element of the heap (which is now in the correct position). We mainly reduce heap size and do not remove element from the actual array
# 4. Heapify the remaining elements of the heap
# 5. Keep doing step2 2-4 until there is only one element left in the heap
# Time complexity: 


def heapify(arr, n, i):
    largest = i
    l = 2*i + 1
    r = 2*i + 2
    
    if l < n and arr[l] > arr[largest]:
        largest = l

    if r < n and arr[r] > arr[largest]:
        largest = r

    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)


def heap_sort(arr):
    n = len(arr)
    # Build heap
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)

    for i in range(n - 1, 0, -1):
        arr[0], arr[i] = arr[i], arr[0] 
        heapify(arr, i, 0)


# Examples
arr = [9, 4, 3, 8, 10, 2, 5] 
heap_sort(arr)
print(arr)
