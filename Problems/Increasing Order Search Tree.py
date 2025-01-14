# Use inorder DFS to make increasing order tree
class Solution:
    def increasingBST(self, root: TreeNode) -> TreeNode:
        res = TreeNode(0)
        curr = res
        
        def inorder(node):
            nonlocal curr  
            if not node:
                return

            inorder(node.left)
            node.left = None 
            curr.right = node
            curr = curr.right 
            inorder(node.right)
    
        inorder(root)
        return res.right
