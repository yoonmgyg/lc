class Solution:
    def kClosest(self, nums: List[int], k: int, target: int):
        heap = []

        for num in nums:
            dist = abs(target - num)
            if len(heap) < k:
                heapq.heappush(heap, (-dist, num))
            elif -heap[0][0] > dist:
                heapq.heappushpop(heap, (-dist, num))
            
        closest = [num[1] for num in heap]
        closest.sort()
        return closest
        
