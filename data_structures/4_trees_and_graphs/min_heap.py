"""
    Minimum Heap Binary Tree Implementation
"""


class MinHeap:
    def __init__(self):
        self.data = [None]
    
    def __str__(self):
        return str(self.data)
    
    def is_empty(self):
        return len(self.data) == 1

    def insert(self, value):
        """
            Insert an element and readjust tree to fulfil heap criteria
        """
        # Insert value to the end of the tree
        if self.is_empty():
            self.data.append(value)
        else:
            self.data.append(value)
            i = len(self.data) - 1
            
            # swap child if it's smaller than it's parent
            while i // 2:
                parent_idx = i // 2
                if self.data[parent_idx] <= self.data[i]:
                    break
                # Swap child and parent
                self.data[parent_idx], self.data[i] = self.data[i], self.data[parent_idx]
                i = parent_idx

            
heap = MinHeap()
values = [4, 50,23,88,90,32,74]
for value in values:
    heap.insert(value)
    print(heap)

# print(heap)
