class Solution(object):
    def runningSum(self, nums):
        output = [0] * len(nums)
        output[0] = nums[0]
        for idx in range(1, len(nums)):
            output[idx] = output[idx - 1] + nums[idx]
        return output     
