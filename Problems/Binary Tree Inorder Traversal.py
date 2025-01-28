# Recursive DFS through children to get inorder results
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        ans = []
        def inorder(root,ans):
            if not root:
                return None
            inorder(root.left,ans)
            ans.append(root.val)
            inorder(root.right,ans)
        inorder(root,ans)
        return ans
