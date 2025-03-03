# Inorder traversal to get distance between nodes
class Solution:
    def minDiffInBST(self, root: Optional[TreeNode]) -> int:
        r = []
        def inorder(node):
            if node:
                inorder(node.left)
                r.append(node.val)
                inorder(node.right)
        inorder(root)
        mini = float('inf')
        for i in range(len(r) - 1):
            mini = min(mini, r[i + 1] - r[i])
        return mini
