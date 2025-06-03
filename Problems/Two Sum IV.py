class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        def helper(root, memo):
            if not root:
                return False  
              
            if (k - root.val) in memo:
                return True
            
            memo.add(root.val)
            
            return helper(root.left, memo) or helper(root.right, memo)
        
        memo = set()
        return helper(root, memo)
