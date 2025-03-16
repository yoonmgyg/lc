
class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        def dfs(root):
            if root is None:
                return []
          
            leaves = dfs(root.left) + dfs(root.right)
            return leaves or [root.val]

        return dfs(root1) == dfs(root2)
        
