class Solution:
    def helper(self,root):
        if not root:
            return None
        root.left = self.helper(root.left)
        root.right = self.helper(root.right)
        if root.left or root.right or root.val == 1:
            return root
        else:
            return None
    def pruneTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        return self.helper(root)
