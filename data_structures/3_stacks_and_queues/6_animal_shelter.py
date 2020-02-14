class Animal:

    def __init__(self, name):
        self.name = name
        self.order = []
    
    def push(self, order):
        self.order.append(order)
    
    def pop(self):
        if self.is_empty():
            raise Exception(f"Out of {self.name} stock")
        return self.order.pop(0)
    
    def is_empty(self):
        return not self.order
    
class Shelter:

    def __init__(self):
        self.dog = Animal("dog")
        self.cat = Animal("cat")
        self.order_num = 0
    
    def __str__(self):
        return f"{self.order_num} Total Animals => Dogs -> {self.dog.order}, Cats -> {self.cat.order}"

    def enqueue(self, name):
        self.order_num += 1
        name = name.lower()
        
        if name == "dog":
            self.dog.push(self.order_num)
       
        elif name == "cat":
            self.cat.push(self.order_num)
        
        else:
            raise Exception("Animal with {name} is not allowed in this shelter")
    
    def dequeue_any(self):
        
        if self.dog.is_empty() and self.cat.is_empty():
            raise Exception("We are sorry, our shelter is empty")
        
        if self.dog.is_empty() and self.cat.order:
            return self.cat.pop()
        
        if self.cat.is_empty() and self.dog.order:
            return self.dog.pop()
        
        if self.dog.order[0] < self.cat.order[0]:
            return self.dog.pop()
        
        else:
            return self.cat.pop()
        
    def dequeue_cat(self):
        if self.cat.is_empty():
            raise Exception("No cats are available at the moment")
        return self.cat.pop()
    
    def dequeue_dog(self):
        if self.dog.is_empty():
            raise Exception("No dogs are available at the moment")
        return self.dog.pop()


shelter = Shelter()
shelter.enqueue("cat")
shelter.enqueue("cat")
shelter.enqueue("dog")
shelter.enqueue("cat")
shelter.enqueue("dog")
shelter.enqueue("cat")
shelter.enqueue("cat")
shelter.enqueue("dog")
shelter.enqueue("dog")
shelter.enqueue("dog")
print(shelter)
shelter.dequeue_any()
print(shelter)
shelter.dequeue_dog()
print(shelter)
shelter.dequeue_dog()
print(shelter)
shelter.dequeue_any()
print(shelter)
shelter.dequeue_any()
print(shelter)
shelter.enqueue("cat")
print(shelter)
shelter.dequeue_any()
print(shelter)

