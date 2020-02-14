"""
    Hash Table Implementation using built-in deque of collections
"""
from collections import deque

class HashTable:

    def __init__(self, table_size):
        self.table_size = table_size
        self.array = [deque() for _ in range(table_size)]

    def __str__(self):
        return str(self.array)


    def insert_data(self, data):
        key = self.get_hash(data)
        self.array[key].append(data)

    def get_hash(self, data):
        return hash(data) % self.table_size
        

    def is_present(self, data):
        key = self.get_hash(data)
        try:
            index = self.array[key].index(data)
            return True
        except ValueError:
            return False



lookup = HashTable(5)

values = [1,2,3,4,5,5,6,6,7,7,8,3,4]

for value in values:
    lookup.insert_data(value)

print(lookup)
print(lookup.is_present(7))