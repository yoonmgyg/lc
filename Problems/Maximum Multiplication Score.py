class Solution:
    def __init__(self):
        self.dp = [[-1e11] * 100001 for _ in range(5)]

    def solve(self, i, j, a, b, n):
        if i == 4:
            return 0
        if j >= n:
            return -1e11
        if self.dp[i][j] != -1e11:
            return self.dp[i][j]
        
        x = a[i] * b[j] + self.solve(i + 1, j + 1, a, b, n)
        y = self.solve(i, j + 1, a, b, n)
        
        self.dp[i][j] = max(x, y)
        return self.dp[i][j]

    def maxScore(self, a, b):
        n = len(b)
        self.dp = [[-1e11] * (n + 1) for _ in range(5)]
        return self.solve(0, 0, a, b, n)
