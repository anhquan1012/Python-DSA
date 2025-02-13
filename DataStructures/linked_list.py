# Three types: regular, circular and doubly linked lists
# Here is implementation for regular linked list
# Methods
# Add: receive data, create new node as root and point to old root, increase size
# Find: find data in the List, return it if exist or return None
# Remove: find node with data and remove it
# Print: print the List


#%%
class Node:
    def __init__(self, d, n=None, p=None):
        self.data = d
        self.next_node = n
        self.prev_node = p

    def __str__(self):
        return f"({str(self.data)})"
    

class LinkedList:
    def __init__(self, r=None):
        '''
        Attributes:
            root (Node): beginning of the List
            size (int): number of nodes in List
        '''
        self.root = r
        self.size = 0

    def add(self, d):
        new_node = Node(d, self.root)
        self.root = new_node
        self.size += 1

    def find(self, d):
        this_node = self.root
        while this_node is not None:
            if this_node.data == d:
                return d
            else:
                this_node = this_node.next_node
        
        return None
    
    def remove(self, d):
        this_node = self.root
        prev_node = None

        while this_node is not None:
            if this_node.data == d:
                if prev_node is not None:
                    prev_node.next_node = this_node.next_node
                else:
                    self.root = this_node.next_node
                self.size -= 1
                return True
            else:
                prev_node = this_node
                this_node = this_node.next_node
        
        return False

    def print(self):
        this_node = self.root
        while this_node is not None:
            print(this_node, end='->')
            this_node = this_node.next_node

        print('None')


# %%
myList = LinkedList()
myList.add(8)
myList.add(10)
myList.add(12)
myList.add(3)
myList.add(2)
myList.add(6)
myList.print()

print("size=", str(myList.size))
myList.remove(10)
myList.print()
print("size=", str(myList.size))
print(myList.find(8))
print(myList.find(9))
print(myList.root)
