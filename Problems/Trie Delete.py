def delete(self, word):
    def _delete(node, index):
        if index == len(word):
            node.is_end = False
            return len(node.children) == 0
        
        char = word[index]
        child = node.children.get(char)
        
        if child is None:
            return False 
        
        should_delete_child = _delete(child, index + 1)
        
        if should_delete_child:
            del node.children[char]
        
        return not node.is_end and len(node.children) == 0
    
    _delete(self.root, 0)
