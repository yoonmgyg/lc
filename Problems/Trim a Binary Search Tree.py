# Recursive dfs to remove nodes greater or lower than value
class Solution:
    def trimBST(self, root: Optional[TreeNode], low: int, high: int) -> Optional[TreeNode]:   
        def trim(node):
            if not node:
                return
            
            if node.val < low:
                return trim(node.right)
            elif high < node.val:
                return trim(node.left)
            
            node.left = trim(node.left)
            node.right = trim(node.right)
            return node
        
        return trim(root)
