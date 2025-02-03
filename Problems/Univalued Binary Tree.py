# DFS through tree and check if values are the same
class Solution:
    def isUnivalTree(self, root: TreeNode) -> bool:
        if not root:
            return True
        
        if root.left and root.val != root.left.val:
            return False
            
        if root.right and root.val != root.right.val:
            return False
        
        return self.isUnivalTree(root.left) and self.isUnivalTree(root.right)
