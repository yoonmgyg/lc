class Solution:
    def printTree(self, root: TreeNode) -> List[List[str]]:
        def get_depth(node):
            if not node: return 0
            return max(get_depth(node.left), get_depth(node.right)) + 1
        
        def insert_value(node, lo, hi, depth=0):
            if not node: return
            mid = (lo + hi) // 2
            output[depth][mid] = str(node.val)
            insert_value(node.left, lo, mid, depth + 1)
            insert_value(node.right, mid, hi, depth + 1)

        depth = get_depth(root)
        output = [[""] * (2**depth - 1) for _ in range(depth)]
        
        insert_value(root, 0, 2**depth - 1)
        return output
