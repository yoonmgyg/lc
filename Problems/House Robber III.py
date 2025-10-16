class Solution:
    def rob(self, root):
        if not root: return 0
        dont_rob, rob_root = self.rob(root.left) + self.rob(root.right), root.val
        if root.left:   rob_root += self.rob(root.left.left)  + self.rob(root.left.right)
        if root.right:  rob_root += self.rob(root.right.left) + self.rob(root.right.right)
        return max(dont_rob, rob_root)
