# Use queue and pop for each person to get coins
class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        piles.sort()
        q = deque(piles)
        res = 0

        while q:
            q.pop() 
            res += q.pop()
            q.popleft() 
        
        return res
