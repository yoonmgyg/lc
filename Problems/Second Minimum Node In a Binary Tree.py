# Recursive dfs to go through numbers and store last 2 values in array
class Solution:
    def findSecondMinimumValue(self, root: Optional[TreeNode]) -> int:
        def dfs(root, ans):
            if not root:
                return

            if root.val < ans[1] and root.val > ans[0]:
                ans[1] = root.val
            else:
                ans[0] = min(ans[0], root.val)

            dfs(root.left, ans)
            dfs(root.right, ans)

        ans = [inf, inf]
        dfs(root, ans)
        return ans[1] if ans[1] != inf else -1
