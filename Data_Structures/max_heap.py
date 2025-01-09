# A heap is a binary tree where every parent is greater than its children (max-heap) or smaller than its children (min-heap)
# Max heap is represented as an array with Arr[0] is root.
# Arr[(i-1)/2] returns parent node, Arr[(2*i)+1] returns left child and Arr[(2*i)+2] returns right child.
# Max heap is fast
# Insert: O(log(n))
# Getmax: O(1)
# Remove max: O(log(n))

#%%
# Public functions: push, peek, pop
# Private functions: __swap, __floatUp, __bubbleDown
class MaxHeap:
    def __init__(self, items=[]):
        self.heap = []
        for item in items:
            self.heap.append(item)
            self.__floatUp(len(self.heap) - 1)

    def push(self, data):
        self.heap.append(data)
        self.__floatUp(len(self.heap) - 1)

    def peek(self):
        if self.heap[0]:
            return self.heap[0]
        else:
            return False
        
    def pop(self):
        if len(self.heap) > 1:
            self.__swap(0, len(self.heap) - 1)
            max = self.heap.pop()
            self.__bubbleDown(0)
        elif len(self.heap) == 1:
            max= self.heap.pop()
        else:
            max = False
        
        return max

    def __swap(self, i, j):
        self.heap[i], self.heap[j] = self.heap[j], self.heap[i]

    def __floatUp(self, index):
        parent = (index-1)//2
        if index <= 0:
            return
        elif self.heap[index] > self.heap[parent]:
            self.__swap(index, parent)
            self.__floatUp(parent)

    def __bubbleDown(self, index):
        left = (index*2) + 1
        right = (index*2) + 2
        largest = index
        if len(self.heap) > left and self.heap[largest] < self.heap[left]:
            largest = left
        if len(self.heap) > right and self.heap[largest] < self.heap[right]:
            largest = right
        if largest != index:
            self.__swap(index, largest)
            self.__bubbleDown(largest)

    def __str__(self):
        return str(self.heap)
    
#%%
m = MaxHeap([95, 3, 21])
m.push(10)
print(m)
print(m.pop())
print(m.peek())
