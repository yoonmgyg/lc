# Sorts colors by looping through nums and using 3 pointers to keep track of sorted regions
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        left = 0
        mid = 0
        right = len(nums) - 1
        while mid <= right:
            if nums[i] == 0:
                nums[left], nums[i] = nums[i], nums[left]
                left += 1
                mid += 1
            elif nums[i] == 1:
                mid += 1
            else:
                nums[right], nums[i] = nums[i], nums[right]
                right -= 1

        
