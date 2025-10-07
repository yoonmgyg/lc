class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        current = 0
        kth = 0
        def dfs(root, k):
            nonlocal current, kth
            if not root or current == k:
                return
            
            left = dfs(root.left, k)
            current += 1
            if current == k:
                kth = root.val
            right = dfs(root.right, k)

        dfs(root, k)
        return kth
