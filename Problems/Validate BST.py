class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def dfs(root, path_min, path_max):
            if not root:
                return True
            if root.val <= path_min or root.val >= path_max:
                return False

            return dfs(root.left, path_min, root.val) and dfs(root.right, root.val, path_max)

        return dfs(root, float("-inf"), float("inf"))
