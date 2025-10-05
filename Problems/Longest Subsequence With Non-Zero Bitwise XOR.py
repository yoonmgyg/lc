class Solution:
    def longestSubsequence(self, nums: List[int]) -> int:
        total = 0
        nonzero = False
        
        for x in nums:
            total ^= x
            if x != 0:
                nonzero = True

        if total == 0:
            if nonzero:
                return len(nums) - 1
            else:
                return 0

        return len(nums)

        
