class Solution:
    def mergeIntervals(self, intervals: List[List[int]]):
        if not intervals:
            return []

        merged = []
        intervals.sort(key=lambda x:x[0])
        merged.append(intervals[0])

        for i in range(1, len(intervals)):
            if merged[-1][1] >= intervals[i][0]:
                merged[-1][1] = max(intervals[i][1], merged[-1][1])
            else:
                merged.append(intervals[i])
        
        return merged
        
