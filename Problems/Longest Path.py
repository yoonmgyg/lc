class Solution:
    def longestUnivaluePath(self, root: Optional[TreeNode]) -> int:
        max_path = 0
        def dfs(root: Optional[TreeNode]):
            nonlocal max_path
            if not root:
                return 0 

            left = dfs(root.left) 
            right = dfs(root.right) 

            left_path = left if root.left and root.left.val == root.val else 0
            right_path = right if root.right and root.right.val == root.val else 0

            max_path = max(max_path, left_path + right_path)

            return 1 + max(left_path, right_path)

        dfs(root)
        return max_path
