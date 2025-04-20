class Solution:
    def frequencySort(self, s: str) -> str:
        freq = Counter(s)

        max_heap = []
        for key, val in freq.items():
            heapq.heappush(max_heap, [-val, key])
        
        res = ""

        for _ in range(len(max_heap)):
            val, key = heapq.heappop(max_heap)
            res += -val * key
        
        return res
