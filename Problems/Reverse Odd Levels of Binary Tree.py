# Reverses odd levels through a dfs which keeps track of levels and swaps if odd
class Solution:
    def reverseOddLevels(self, root):
        def dfs(leftChild, rightChild, level):
            if not leftChild or not rightChild:
                return
            if level % 2 == 0:
                leftChild.val, rightChild.val = rightChild.val, leftChild.val
            dfs(leftChild.left, rightChild.right, level + 1)
            dfs(leftChild.right, rightChild.left, level + 1)

        dfs(root.left, root.right, 0)
        return root
