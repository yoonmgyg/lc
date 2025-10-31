class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        current = float('inf')
        for price in prices:
            if price < current:
                current = price
            elif price > current:
                profit += price - current
                current = price
        return profit
