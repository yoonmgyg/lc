class Solution:
    def maximumScore(self, nums: List[int]) -> int:
        n = len(nums)
        prefix = [0] * n
        prefix[0] = nums[0]

        for i in range(1, n):
            prefix[i] = prefix[i-1] + nums[i]

        max_score = float('-inf')
        min_suffix = nums[-1]
        for i in range(n-2, -1, -1):
            max_score = max(max_score, prefix[i] - min_suffix)
            min_suffix = min(min_suffix, nums[i])

        return max_score
