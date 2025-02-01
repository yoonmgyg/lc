# Sort nums and keep track of min and max values
class Solution:
    def findNonMinOrMax(self, nums: List[int]) -> int:
        n = len(nums)
        if n <= 2:
            return -1

        nums.sort()
        min_val = nums[0]
        max_val = nums[-1]

        for i in range(1, n - 1):
            if nums[i] != min_val and nums[i] != max_val:
                return nums[i]

        return -1
