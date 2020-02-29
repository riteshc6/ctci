"""
    Minimum Heap Binary Tree Implementation
    Refer https://www.cs.cmu.edu/~tcortina/15-121sp10/Unit06B.pdf for understanding min heap concept
"""


class MinHeap:
    def __init__(self):
        self.data = [None]  # First element is not used in heap
    
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

    def extract_min(self):
        """
            Pops minimum value from heap and readjusts tree to satisfy heap order
        """
        if self.is_empty():
            raise Exception("Heap is Empty")

        smaller_child_idx = None
        left_child_idx = None
        right_child_idx = None
        
        min_elem = self.data[1]
        self.data[1] = self.data.pop(-1)    # Move last element to the top 
        parent_idx = 1
        length = len(self.data) - 1

        while True:
            left_child_idx = 2 * parent_idx if (2 * parent_idx) <= length else None
            right_child_idx = 2 * parent_idx + 1 if (2 * parent_idx + 1) <= length else None
            smaller_child_idx = self.find_smaller_child(left_child_idx, right_child_idx)

            if smaller_child_idx:
                if self.data[parent_idx] > self.data[smaller_child_idx]:
                    self.data[parent_idx], self.data[smaller_child_idx] = self.data[smaller_child_idx], self.data[parent_idx]
                    parent_idx = smaller_child_idx
                else:
                    break
            else:
                break
        return min_elem

    def find_smaller_child(self, left_child_idx, right_child_idx):
        """
            Find smallest of the two childs if they exist else return none
        """

        # Return None if no child nodes
        if not left_child_idx and  not right_child_idx:
            return None
        
        if not left_child_idx:
            return right_child_idx
        
        if not right_child_idx:
            return left_child_idx
        
        if self.data[right_child_idx] < self.data[left_child_idx]:
            return right_child_idx
        else:
            return left_child_idx


            
heap = MinHeap()
values = [4, 50,23,88,90,32,74]
for value in values:
    heap.insert(value)

print(heap)

heap.extract_min()
print(heap)
heap.extract_min()
print(heap)
