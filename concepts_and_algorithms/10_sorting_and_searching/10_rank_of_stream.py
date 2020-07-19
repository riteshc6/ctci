class RankNode:
    def __init__(self, d: int):
        self.left_size = 0
        self.left = None
        self.right = None
        self.data = d

    def insert(self, d: int):
        if d <= self.data:
            if self.left == None:
                self.left = RankNode(d)
            else:
                self.left.insert(d)
            self.left_size += 1
        else:
            if self.right == None:
                self.right = RankNode(d)
            else:
                self.right.insert(d)
    
    def get_rank(self, d: int):
        if d == self.data:
            return self.left_size
        
        elif d < self.data:
            if self.left == None: return -1
            else: return self.left.get_rank(d)
        
        else:
            right_rank = -1 if self.right == None else self.right.get_rank(d)
            if right_rank == -1: return -1
            else: return self.left_size + 1 + right_rank


if __name__ == "__main__":
    import random

    root = None

    def track(number: int):
        global root
        if root == None:
            root = RankNode(number)
        else:
            root.insert(number)

    def get_rank_of_number(number: int):
        global root
        return root.get_rank(number)
    
    stream_list = []
    for _ in range(20):
        integer = random.randint(-10, 10)
        stream_list.append(integer)
        track(integer)
    
    tracker = [0] * len(stream_list)
    for i in range(len(stream_list)):
        v = stream_list[i]
        rank1 = root.get_rank(stream_list[i])
        tracker[rank1] = v	
    

    for i in range(len(tracker) - 1):
        if (tracker[i] != 0 and tracker[i + 1] != 0):
            if (tracker[i] > tracker[i + 1]):
                print("ERROR at " + str(i))
    
    # NOTE: Duplicate elements will have only one rank
    print("Array: ", sorted(stream_list))
    print("Ranks: ", tracker)

