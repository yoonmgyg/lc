# Creates max bin tree by getting max value of nums and recursively calling for all numbers other than the max
def constructMaximumBinaryTree(self, nums: List[int]) -> TreeNode:
    if len(nums) == 0:
        return None
      
    max_value = max(nums)
    max_index = nums.index(max_value)
    root = TreeNode(max_value)
    
    root.left = self.constructMaximumBinaryTree(nums[ : max_index])
    root.right = self.constructMaximumBinaryTree(nums[max_index + 1 : ])
    return root
