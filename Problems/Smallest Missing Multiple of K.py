class Solution:
    def missingMultiple(self, nums: List[int], k: int) -> int:
        nums.sort()
        smallest = k
        i = 0

        while i < len(nums):
            if nums[i] > smallest:
                break

            if nums[i] == smallest:
                smallest += k

            i += 1

        return smallest
