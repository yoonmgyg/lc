
class Solution:
    def rightmostNode(self, root: TreeNode):
        if not root:
            return []
        queue = deque([root])
        rightmost = []
        while queue:
            level_size = len(queue)
            for i in range(level_size):
                curr_node = queue.popleft()
                if (i == level_size - 1):
                    rightmost.append(curr_node.val)
                if curr_node.left:
                    queue.append(curr_node.left)
                if curr_node.right:
                    queue.append(curr_node.right)
        return rightmost
