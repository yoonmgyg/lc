class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        
        dp_hold, dp_not_hold = -float('inf'), 0
        
        for stock_price in prices:
            prev_hold, prev_not_hold = dp_hold, dp_not_hold
            dp_not_hold = max(prev_not_hold, prev_hold + stock_price)
            dp_hold = max(prev_hold, prev_not_hold - stock_price - fee)
        
        return dp_not_hold
