class Solution:
    def level_order_sum(self, root: TreeNode):
        if not root:
            return []

        res = []
        queue = deque([root])
        while queue:
            level = len(queue)
            sum = 0
            for i in range(level):
                curr_node = queue.popleft()
                sum += curr_node.val

                if curr_node.left:
                    queue.append(curr_node.left)

                if curr_node.right:
                    queue.append(curr_node.right)
            res.append(sum)
        return res
