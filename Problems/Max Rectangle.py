from typing import List

class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        if not matrix or not matrix[0]:
            return 0
        
        n = len(matrix[0])
        height = [0] * n
        result = 0

        for row in matrix:
            for j in range(n):
                if row[j] == '1':
                    height[j] += 1
                else:
                    height[j] = 0
            
            result = max(result, self.largestRectangleArea(height))
        
        return result

    def largestRectangleArea(self, heights: List[int]) -> int:
        if not heights:
            return 0
        
        n = len(heights)
        max_area = 0
        less_from_left = [-1] * n
        less_from_right = [n] * n

        for i in range(1, n):
            p = i - 1
            while p >= 0 and heights[p] >= heights[i]:
                p = less_from_left[p]
            less_from_left[i] = p

        for i in range(n - 2, -1, -1):
            p = i + 1
            while p < n and heights[p] >= heights[i]:
                p = less_from_right[p]
            less_from_right[i] = p

        for i in range(n):
            width = less_from_right[i] - less_from_left[i] - 1
            max_area = max(max_area, heights[i] * width)

        return max_area
