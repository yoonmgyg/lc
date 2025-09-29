class Solution:
    def zig_zag(self, root: TreeNode):
        if not root:
            return []
        
        queue = deque([root])
        right = True
        res = []
        while queue:
            level_size = len(queue)
            current_level = []
            for i in range(level_size):
                current = queue.popleft()
                current_level.append(current.val)
                if current.left :
                    queue.append(current.left)
                if current.right:
                    queue.append(current.right)
            right = not right
            if right:
                current_level[::-1]
            res.append(current_level)
        return res
