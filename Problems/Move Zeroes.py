# Keeps track of each zero and swaps with the next non-zero
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        next_zero = 0

        for i in range(len(nums)):
            if nums[i] != 0:
                nums[next_zero], nums[i] = nums[i], nums[next_zero]
                next_zero += 1
        
