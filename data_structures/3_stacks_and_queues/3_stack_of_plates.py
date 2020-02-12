class Stack:

    def __init__(self, threesold):
        self.threesold = threesold
        self.values = []
        self.length = 0

    def is_full(self):
        return self.threesold == self.length
    
    def is_empty(self):
        return not self.length
    
    def push(self, data):
        if self.is_full():
            raise Exception("Stack is full")

        self.values.append(data)
        self.length += 1
    
    def pop(self):
        if self.is_empty():
            raise Exception("Stack is Empty")
        data = self.values.pop(-1)
        self.length -= 1
        return data


class SetOfStacks:

    def __init__(self, threesold):
        self.stacks = []
        self.threesold = threesold
    
    def __str__(self):
        string = str(len(self.stacks))
        for idx, stack in enumerate(self.stacks):
            string += f" = {idx} -> {stack.values},"
        return string
    
    def push(self, data):
        if self.is_empty():
            stack = Stack(self.threesold)
            stack.push(data)
            self.stacks.append(stack)
        else:
            stack = self.stacks[-1]
            if stack.is_full():
                stack = Stack(self.threesold)
                stack.push(data)
                self.stacks.append(stack)
            else:
                stack.push(data)

    def pop(self):
        if self.is_empty():
            raise Exception("Stack is empty")
        stack = self.stacks[-1]
        data = stack.pop()
        if stack.is_empty():
            self.stacks.pop(-1)
        return data

    def is_empty(self):
        return not self.stacks


    def popAt(self, stack_index):
        stack = self.stacks[stack_index]
        data = stack.pop()
        if stack.is_empty():
            self.stacks.pop(stack_index)
        return data


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


