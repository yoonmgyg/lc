class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def eating_time(r):
            time = 0
            for i in piles:
                time += (i + r - 1) // r
            return time
        
        left = 1
        right = max(piles)

        while (left < right):
            mid = (left + right) // 2
            if eating_time(mid) <= h:
                right = mid
            else:
                left = mid + 1

        return left

        
