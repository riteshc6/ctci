class SetOfStacks:

    def __init__(self, threesold):
        self.values = []
        self.stacks_size = []
        self.threesold = threesold
    
    def __str__(self):
        return f"Data -> {self.values}, stacks -> {self.stacks_size}"
    
    def push(self, data):
        self.values.append(data)
        if self.is_empty():
            self.stacks_size.append(1)
        else:
            if self.is_stack_full():
                self.stacks_size.append(1)
            else:
                self.stacks_size[-1] += 1

    def pop(self):
        if self.is_empty():
            raise Exception("Stack is empty")
        data = self.values.pop(-1)
        self.update_stacks_size()
        return data
    
    def update_stacks_size(self):
        if self.stacks_size[-1] == 1:
            self.stacks_size.pop(-1)
        else:
            self.stacks_size[-1] -= 1

    def is_empty(self):
        return not len(self.stacks_size)
    
    def is_stack_full(self):
        return self.stacks_size[-1] == self.threesold

    def popAt(self, stack_index):
        values_index = self.get_data_index(stack_index)
        data = self.values.pop(values_index)
        self.update_stacks_size()
        return data
    
    def get_data_index(self, stack_index):
        offset = (stack_index * self.threesold) - 1
        return offset + self.stacks_size[stack_index]


stacks = SetOfStacks(3)
data = [3,4,5,7,10,12,14,1]
for value in data:
    stacks.push(value)
    print(stacks)

stacks.popAt(1)
print(stacks)
stacks.popAt(1)
print(stacks)
stacks.popAt(0)
print(stacks)

# for _ in range(len(data)):
#     stacks.pop()
#     print(stacks)


