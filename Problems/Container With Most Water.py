# Gets the contianer with most water through 2 pointers moving towards the center with lower height
# T: O(n)
# S: O(1)
class Solution:
    def maxArea(self, height: List[int]) -> int:
        left = 0
        right = len(height) - 1
        maxArea = 0
        # Loop until pointers meet
        while (left < right):
            # Calculate are and update with greater
            maxArea = max(maxArea, min(height[left], height[right]) * (right - left))
            if (height[left] > height[right]):
                right -= 1
            else:
                left += 1
        
        return maxArea
