class Solution:
    def largestRectangleArea(self, heights: List[int]):
        stack = []
        max_area = 0
        i = 0
        for i, h in enumerate(heights + [0]):
            while stack and heights[stack[-1]] > h: # loop until lower bar is found
                top = stack.pop()
                right = i - 1
                left = stack[-1] if stack else -1
                max_area = max(max_area, heights[top] * (right - left)) # calculate area with current height and distance to previous bar
            stack.append(i)
        return max_area
