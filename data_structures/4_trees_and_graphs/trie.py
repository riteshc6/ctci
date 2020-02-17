"""
    Trie data structure implementation for word
"""

class Trie:

    def __init__(self):
        self.nodes = dict()
        self.is_leaf = False    # Checks the end of the word
    
    def insert(self, word):
        cur = self
        for char in word:
            if char not in cur.nodes:
                cur.nodes[char] = Trie()
            cur = cur.nodes[char]
        cur.is_leaf = True
    
    def find(self, word):
        cur = self
        for char in word:
            print(cur.nodes.keys())
            if char not in cur.nodes:
                return False
            cur = cur.nodes[char]
        return cur.is_leaf
    

    
trie = Trie()
trie.insert("rob")
trie.insert("roger")
trie.insert("angela")

print(trie.find("rob"))
print(trie.find("ang"))
