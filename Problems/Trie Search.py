def search(self, word):
    node = self.root
    
    for char in word:
        if char not in node.children:
            return False
        node = node.children[char]
    
    return node.is_end
