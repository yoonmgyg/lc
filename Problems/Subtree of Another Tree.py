class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not subRoot:
            return True
        if not root:
            return False

        if self.isSametree(root, subRoot):
            return True
        
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)

    def isSametree(self, root, subRoot):
        if not root and not subRoot:
            return True
        if not root or not subRoot: 
            return False

        if root.val == subRoot.val:
            return self.isSametree(root.left, subRoot.left) and self.isSametree(root.right, subRoot.right)
        return False
        
