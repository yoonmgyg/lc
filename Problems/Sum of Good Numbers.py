class Solution:
    def sumOfGoodNumbers(self, nums: list[int], k: int) -> int:
        n = len(nums)
        good_sum = 0

        for i, num in enumerate(nums):
            if i - k >= 0 and num <= nums[i - k]:
                continue
            if i + k < n and num <= nums[i + k]:
                continue
            good_sum += num

        return good_sum
