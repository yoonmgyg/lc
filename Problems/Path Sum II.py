class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        def dfs(root: Optional[TreeNode], targetSum: int, targetList: List[int]):
            if not root:
                return 
            
            targetList.append(root.val)
            targetSum -= root.val
            if not root.left and not root.right and targetSum == 0:
                res.append(targetList[:])
            
            dfs(root.left, targetSum, targetList)
            dfs(root.right, targetSum, targetList)
            targetList.pop()

        res = []
        dfs(root, targetSum, [])
        return res
        
