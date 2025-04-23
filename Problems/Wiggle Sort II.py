class Solution(object):
    def wiggleSort(self, nums):
        nums.sort()
        mid = (len(nums) + 1) // 2
        left, right = nums[:mid][::-1], nums[mid:][::-1]
        nums[::2], nums[1::2] = left, right
