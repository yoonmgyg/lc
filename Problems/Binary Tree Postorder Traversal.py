class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []

        result = []
        stack1 = [root]
        stack2 = []

        while stack1:
            current = stack1.pop()
            stack2.append(current)

            if current.left:
                stack1.append(current.left)
            if current.right:
                stack1.append(current.right)

        while stack2:
            result.append(stack2.pop().val)

        return result
