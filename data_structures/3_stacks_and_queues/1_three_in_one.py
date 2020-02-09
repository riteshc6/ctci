# Implement a multi-stack data structure using a single array as your data
# Provides functionality to push pop data to any of the stacks basead on the availability

class ThreeStack:
    """
        stacks_size array is used to track the size of each stack, values array is used to 
        store the values of all stacks
    """
    def __init__(self, stack_size):
        self.num_stacks = 3
        self.stack_size = stack_size
        self.values = [0] * (self.stack_size * self.num_stacks)
        self.stacks_size = [0] * self.num_stacks

    def __str__(self):
        return str(self.values) + str(self.stacks_size)

    
    def push(self, stack_num, data):
        """
            Adds data to the stack provided by user and updates stack size of the coresponding stack
        """
        if self.is_stack_full(stack_num):
            raise Exception("Stack Overflow")
        top_index = self.top_index_of_stack(stack_num)
        self.values[top_index + 1] = data
        stack_index = stack_num - 1
        self.stacks_size[stack_index] += 1

    def pop(self, stack_num):
        """
            Removes data from top of given staack and returns it
        """
        if self.is_stack_empty(stack_num):
            raise Exception("Stack is empty")
        top_index = self.top_index_of_stack(stack_num)
        data = self.values[top_index]
        self.values[top_index] = 0
        stack_index = stack_num - 1
        self.stacks_size[stack_index] -= 1
        return data

    def peek(self, stack_num):
        """
            Returns top value for the stack given
        """
        if self.is_stack_empty(stack_num):
            raise Exception("Stack is empty")
        top_index = self.top_index_of_stack(stack_num)
        return self.values[top_index]

    def is_stack_empty(self, stack_num):
        stack_index = stack_num - 1
        return self.stacks_size[stack_index] == 0

    def is_stack_full(self, stack_num):
        stack_index = stack_num - 1
        return self.stacks_size[stack_index] == self.stack_size

    def top_index_of_stack(self, stack_num):
        stack_index = stack_num - 1
        stack_offset = (stack_index * self.stack_size) 
        return stack_offset + self.stacks_size[stack_index] - 1


triple_stack = ThreeStack(2)
triple_stack.push(2, 3)
triple_stack.push(2, 4)
print(triple_stack)
triple_stack.push(3, 2)
print(triple_stack)
print(triple_stack.pop(2))
print(triple_stack)
