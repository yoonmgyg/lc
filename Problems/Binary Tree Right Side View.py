class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        
        res = []
        queue = deque()
        queue.append(root)
        while queue:
            level_len = len(queue)
            for i in range(level_len):
                current = queue.popleft()
                if i == level_len - 1:
                    res.append(current.val)
                
                if current.left:
                    queue.append(current.left)
                if current.right:
                    queue.append(current.right)
        
        return res
