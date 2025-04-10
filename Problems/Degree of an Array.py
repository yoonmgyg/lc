# Use dict map to get array indices and find subarray
class Solution(object):
    def findShortestSubArray(self, nums):
        c = defaultdict(list)
        for i, n in enumerate(nums):
            c[n].append(i)        
        degree = max([len(x) for x in c.values()])
        
        result = len(nums)
        for indices in c.values():
            if len(indices) == degree:
                result = min(result, indices[-1] - indices[0])
        return result + 1         
