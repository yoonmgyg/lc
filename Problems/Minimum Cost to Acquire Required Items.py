class Solution:
    def minimumCost(self, cost1: int, cost2: int, costBoth: int, need1: int, need2: int) -> int:
        candidates = {0, need1, need2}
        limit = max(need1, need2)

        ans = float('inf')
        for x in candidates:
            if x < 0 or x > limit:
                continue
            rem1 = max(0, need1 - x)
            rem2 = max(0, need2 - x)
            total_cost = x * costBoth + rem1 * cost1 + rem2 * cost2
            ans = min(ans, total_cost)

        return ans
