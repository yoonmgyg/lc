class KthLargest:
    def __init__(self, k: int, nums: List[int]):
        n = len(nums)
        self.k = k
        self.heap = []
        for i in range(n):
            if len(self.heap) < k:
                heapq.heappush(self.heap, nums[i])
            elif nums[i] > self.heap[0]:
                heapq.heapreplace(self.heap, nums[i])

    def add(self, val: int) -> int:
        if len(self.heap) < self.k:
            heapq.heappush(self.heap, val)
        elif val > self.heap[0]:
            heapq.heappushpop(self.heap, val)
        return self.heap[0]
