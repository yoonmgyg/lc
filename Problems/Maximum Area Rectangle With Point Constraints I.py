class Solution:
    def maxRectangleArea(self, points: List[List[int]]) -> int
        def findArea(nums: tuple)-> int:
            (x1,y1), (x2,y2), (x3,y3), (x4,y4) = nums 
            if not (x1,x3, y1,y2) == (x2,x4, y3,y4): return -1 
            for point in points:
                if point in nums: continue 
                if x1 <= point[0] <= x3 and y1 <= point[1] <= y2: return -1
            return (x3 - x1) * (y2 - y1)
        points.sort()
        return max(map(findArea, combinations(points,4)))
