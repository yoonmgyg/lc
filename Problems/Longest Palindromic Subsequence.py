class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        def dp(i, j):
            if i == j:
                return 1
            elif i > j:
                return 0
            if s[i] == s[j]:
                return 2 + dp(i + 1, j - 1)
            else:
                return max(dp(i + 1, j), dp(i, j - 1))
            
        s = list(s)
        return dp(0, len(s) - 1)
