class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        max_stones = [-s for s in stones]
        heapq.heapify(max_stones)
        while len(max_stones) > 1:
            heavy_one = heapq.heappop(max_stones)
            heavy_two = heapq.heappop(max_stones)
            if heavy_two > heavy_one:
                heapq.heappush(max_stones, heavy_one - heavy_two)
        
        return abs(max_stones[0]) if max_stones else 0
