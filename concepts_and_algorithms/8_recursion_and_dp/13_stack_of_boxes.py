from typing import List

class Box:
    def __init__(self, w: int, h: int, d: int):
        self.width = w
        self.height = h
        self.depth = d
    
    def can_be_above_bottom(self, b):
        if not b:
            return True
        
        if self.width < b.width and self.height < b.height and self.depth < b.depth:
            return True
        
        return False
    
    def to_string(self):
        return f"Box(width: {self.width}, height: {self.height}, depth: {self.depth})"


def create_stack(boxes: List[Box]):
    boxes = sorted(boxes, key = lambda a: a.height, reverse=True)
    max_height = 0
    stack_map = [0] * len(boxes)
    for i in range(len(boxes)):
        height = _create_stack(boxes, i, stack_map)
        max_height = max(height, max_height)
    
    return max_height

def _create_stack(boxes: List[Box], bottom_index: int, stack_map: list):
    if bottom_index < len(boxes) and stack_map[bottom_index] > 0:
        return stack_map[bottom_index]
    bottom = boxes[bottom_index]
    max_height = 0
    for i in range(bottom_index + 1, len(boxes)):
        if boxes[i].can_be_above_bottom(bottom):
            height = _create_stack(boxes, i, stack_map)
            max_height = max(height, max_height)
    
    max_height += bottom.height
    stack_map[bottom_index] = max_height
    return max_height


if __name__ == "__main__":
    boxes = [Box(6, 4, 4), Box(6, 5, 6), Box(5, 5, 5), Box(7, 7, 7), Box(4, 2, 2), Box(9, 10, 8)]
    height = create_stack(boxes)
    print(height)
