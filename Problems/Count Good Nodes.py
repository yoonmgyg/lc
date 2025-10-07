class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        count = 0
        def dfs(root, path_max):
            nonlocal count
            if not root:
                return 0
            
            if root.val >= path_max:
                count += 1

            left = dfs(root.left, max(path_max, root.val))
            right = dfs(root.right, max(path_max, root.val))
        
        dfs(root, root.val)
        return count
