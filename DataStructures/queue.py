# FIFO data structure
# Queues are good for modeling anything you wait in line for
# Enqueue on one end, and dequeue from the other end

#%%
class Queue:
    def __init__(self):
        self.s1 = list()
        self.s2 = list()

    def peek(self):
        if len(self.s1) > 0:
            return self.s1[-1]
        else:
            return
        
    def enqueue(self, data):
        for i in range(len(self.s1)):
            item = self.s1.pop()
            self.s2.append(item)
        self.s1.append(data)
        for i in range(len(self.s2)):
            item = self.s2.pop()
            self.s1.append(item)

    def dequeue(self):
        if len(self.s1) > 0:
            return self.s1.pop()
        else:
            return
    
    def print_queue(self):
        if len(self.s1) == 0:
            print("Queue Empty")
            return
        for i in range(len(self.s1) - 1,0,-1):
            print(f'{self.s1[i]} <<-- ',end='')
        print(self.s1[0])
        return
    
#%%
my_queue = Queue()
my_queue.enqueue(1)
my_queue.enqueue(8)
my_queue.enqueue(3)
my_queue.print_queue()
print(my_queue.dequeue())
my_queue.print_queue()
print(my_queue.peek())
print(my_queue.dequeue())
print(my_queue.dequeue())
print(my_queue.dequeue())
