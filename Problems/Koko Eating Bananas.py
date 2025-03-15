class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        n = len(piles)
        s = sum(piles)
        l = math.ceil(s / h) 
        r = max(piles) if h == n else int((s - n) / (h - n) + 1)

        while l <= r:
            k = (l + r) // 2

            hours = 0 
            for bananas in piles:
                hours += (bananas // k) + 1 if bananas % k else bananas // k

            if hours > h:
                l = k + 1
            else:
                r = k - 1
        return l
