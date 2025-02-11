# Deletes node by setting next to one after
class Solution:
    def deleteNode(self, node):
        if node is None or node.next is None:
            return
        
        node.val = node.next.val
        node.next = node.next.next
