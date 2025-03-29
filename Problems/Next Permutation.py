class Solution:
    def nextPermutation(self, nums):
        # find the first index 'i' from the right where nums[i] is less than its next element
        i = len(nums) - 2
        while i >= 0 and nums[i] >= nums[i + 1]:
            i -= 1

        # if such an index is found, there's a lexicographically higher permutation
        if i >= 0:
            # find the first element from the right that is greater than nums[i]
            j = len(nums) - 1
            while nums[j] <= nums[i]:
                j -= 1
            # swap the found element with nums[i]
            nums[i], nums[j] = nums[j], nums[i]

        # reverse the subarray from i+1 to the end to get the smallest order
        left, right = i + 1, len(nums) - 1
        while left < right:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
            right -= 1
