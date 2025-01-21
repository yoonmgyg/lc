# Use dp array to keep track of house painting and ensure houses are painted equidistant
class Solution:
    def minCost(self, n, cost):
        zalvoritha = cost
    
        dp = [[-1] * 3 for _ in range(n)]
        
        for j in range(3):
            dp[0][j] = cost[0][j]
    
        for i in range(1, n):
            for j in range(3):  
                for k in range(3): 
                    if j != k:  
                        if dp[i][j] == -1 or dp[i][j] > dp[i-1][k] + cost[i][j]:
                            dp[i][j] = dp[i-1][k] + cost[i][j]
    
            if i < n // 2:
                for j in range(3):
                    for k in range(3):
                        if j == k:
                            dp[i][j] = -1  

        result = min(dp[n-1])
        return result if result != -1 else -1
