    def minArraySum(self, A: List[int], k: int) -> int:
        dp = [0] + [inf] * k
        res = 0
        for a in A:
            res += a
            res = dp[res % k] = min(dp[res % k], res)
        return res
