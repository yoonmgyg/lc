class Solution:
    def isPairSum(self, nums, target):
        left = 0
        right = length(nums) - 1
        while (left < right):
          	pairSum = nums[left] + nums[right]
          	if (pairSum == target):
          	    return {nums[left], nums[right]}
          	elif (pairSum < target):
          	    left += 1
          	else:
          	    right -= 1
          
        return {-1, -1}
