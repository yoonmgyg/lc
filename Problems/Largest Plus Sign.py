class Solution:
    def orderOfLargestPlusSign(self, n: int, mines: List[List[int]]) -> int:
        mines_set = set()
        for x, y in mines:
            mines_set.add((x, y))
        
        dp = [[[0] * 4 for _ in range(n + 1)] for _ in range(n + 1)]
        max_res = 0

        for r in range(n - 1, -1, -1):
            for c in range(n - 1, -1, -1):
                for direction in [1, 3]:
                    if (r, c) in mines_set:
                        continue
                    if direction == 1:
                        dp[r][c][direction] = 1 + dp[r][c + 1][1]
                    elif direction == 3:
                        dp[r][c][direction] = 1 + dp[r + 1][c][3]

        for r in range(n):
            for c in range(n):
                for direction in [0, 2]:
                    if (r, c) in mines_set:
                        continue
                    if direction == 0:
                        dp[r][c][direction] = 1 + dp[r][c - 1][0]
                    elif direction == 2:
                        dp[r][c][direction] = 1 + dp[r - 1][c][2]

                max_res = max(max_res, min(dp[r][c]))
                
        return max_res
        
