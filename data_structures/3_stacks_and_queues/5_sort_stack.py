from stack_ll import Stack

def sort(stack):

    temp_stack = Stack()

    while not stack.is_empty():
        data = stack.pop()

        while not temp_stack.is_empty():
            if temp_stack.peek() > data:
                temp_data = temp_stack.pop()
                stack.push(temp_data)
            else:
                break
        temp_stack.push(data)
    
    while not temp_stack.is_empty():
        data = temp_stack.pop()
        stack.push(data)
    
    return stack

stack = Stack()
values = [3,2,5,7,1,10,24]
for value in values:
    stack.push(value)
print(stack)
print(sort(stack))