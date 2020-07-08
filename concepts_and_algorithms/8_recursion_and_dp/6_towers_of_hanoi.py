# NOTE: Initially one of the towers is filled completely and rest 2 are empty

from collections import deque

class Tower:

    def __init__(self, index: int):
        self.disks = deque()
        self.index = index
    
    def add(self, d: int) -> None:
        if self.disks:
            if self.disks[0] <= d:
                print("Error in placing disk")
            else:
                self.disks.appendleft(d)
        else:
            self.disks.appendleft(d)
    
    def move_top_to(self, t):
        top = self.disks.popleft()
        t.add(top)
    
    def move_disks(self, n: int, destination, buffer):
        if n > 0:
            self.move_disks(n - 1, buffer, destination)
            self.move_top_to(destination)
            buffer.move_disks(n - 1, destination, self)

n = 3   # no. of towers
towers = [Tower(i) for i in range(n)]
N = 5   # no. of disks
# Adding disks in ascending order
[towers[0].add(i) for i in reversed(range(N))]

towers[0].move_disks(N, towers[2], towers[1])
print(towers[2].disks)