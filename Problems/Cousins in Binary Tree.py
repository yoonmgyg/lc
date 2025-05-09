class Solution:
    def isCousins(self, root: TreeNode, x: int, y: int) -> bool:
    		res = [] 
        def dfs(node, parent, depth):
            if not node:
                return
            if node.val == x or node.val == y:
                res.append((parent, depth))
            dfs(node.left, node, depth + 1)
            dfs(node.right, node, depth + 1)
            
        dfs(root, None, 0)

        node_x, node_y = res  
        return node_x[0] != node_y[0] and node_x[1] == node_y[1]
