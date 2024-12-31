# Gets the maximum height  seen by two pointers and calculates the water subtracting from the min
class Solution:
    def trap(self, height: List[int]) -> int:
        left = 0
        right = len(height) - 1
        leftMax = height[left]
        rightMax = height[right]
        water = 0

        while left + 1 < right:
            if rightMax < leftMax:
                left += 1
                if heights[left] > leftMax:
                    leftMax = max(leftMax, heights[left])
                else:
                    water += leftMax - heights[left]
            else:
                right -= 1
                if heights[right] > rightMax:
                    rightMax = heights[right]
                else:
                    water += rightMax - heights[right]

        return water
        
