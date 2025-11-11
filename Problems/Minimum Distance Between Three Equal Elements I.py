class Solution:
    def minimumDistance(self, nums: List[int]) -> int:
        pos = collections.defaultdict(list)
        for i, v in enumerate(nums):
            pos[v].append(i)

        best = float('inf')
        for indices in pos.values():
            if len(indices) < 3:
                continue
            for i in range(len(indices) - 2):
                span = indices[i+2] - indices[i]   
                best = min(best, 2 * span)         

        return -1 if best == float('inf') else best
