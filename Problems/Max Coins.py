class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        n = len(nums)
        nums = nums + [1]
        dp = [[0 for _ in range(n+1)] for _ in range(n+1)]

        for i in range(n):
            dp[i][i] = nums[i] * nums[i-1] * nums[i+1]

        for i in range(1, n):
            for l in range(n):
                if i + l == n:
                    break
                r = i + l
                for k in range(l, r+1):
                    dp[l][r] = max(dp[l][r], dp[l][k-1] + dp[k+1][r] + nums[k] * nums[l-1] * nums[r + 1])


        return dp[0][n-1]
