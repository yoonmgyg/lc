class Solution:
    def checkElement(self, nums: List[int], val: int) -> int:
        n = len(nums)
        left = 0
        right = n - 1
        k = 0

        while (left <= right):
            if nums[left] == val:
                nums[left], nums[right] = nums[right], nums[left]
                k += 1
                right -= 1
            else:
                left += 1

        return n - k
