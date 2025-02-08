# Create iterator class by using generator function to create nodes inorder
def __init__(self, root):
    self.last = root
    while self.last and self.last.right:
        self.last = self.last.right
    self.current = None
    self.g = self.iterate(root)

def hasNext(self):
    return self.current is not self.last

def next(self):
    return next(self.g)
    
def iterate(self, node):
    if node is None:
        return
    for x in self.iterate(node.left):
        yield x
    self.current = node
    yield node.val
    for x in self.iterate(node.right):
        yield x
