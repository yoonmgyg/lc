# Use bin search through sorted coins and get prefix sum of coins to find maximum from K consecutive bags
class Solution:
    def maximumCoins(self, coins: List[List[int]], k: int) -> int:
        coins.sort()
        ans = 0
        prefix = [0]
        vals = []
        for l, r, c in coins: 
            prefix.append(prefix[-1] + c*(r-l+1))
            vals.extend([l+k-1, r])
            
        def fn(x): 
            i = bisect_right(coins, x, key=lambda x: x[0]) - 1
            if i < 0: 
                return 0 
            return prefix[i] + (min(x, coins[i][1]) - coins[i][0] + 1) * coins[i][2]
        
        return max(fn(r) - fn(r-k) for r in sorted(vals))
