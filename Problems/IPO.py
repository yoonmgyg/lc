class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        min_cap_heap = [(capital[i], profits[i]) for i in range(len(profits))]
        heapq.heapify(min_cap_heap)

        max_profit_heap = []

        for _ in range(k):
            while min_cap_heap and min_cap_heap[0][0] <= w:
                cap, profit = heapq.heappop(min_cap_heap)
                heapq.heappush(max_profit_heap, -profit)  # Negate to simulate max-heap

            if not max_profit_heap:
                break
            
            w += -heapq.heappop(max_profit_heap)

        return w
