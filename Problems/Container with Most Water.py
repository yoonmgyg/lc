class Solution:
    def max_area(self, heights):
        res = 0
        left = 0
        right = len(heights) - 1
        while (left < right):
            area = min(heights[left], heights[right]) * (right - left)
            if (heights[left] > heights[right]):
                right -= 1
            else:
                left += 1
            res = max(res, area)
    
        return res
