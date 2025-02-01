# Loop through each element and add in hourglass shape, then compare with current max hourglass
class Solution:
    def maxSum(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        max_sum = float("-inf")
        
        for row in range(rows-3+1): 
            for col in range(1, cols-2+1):
                if row + 2 <= rows and col+1 <= cols:
                    ur = grid[row][col-1] + grid[row][col] + grid[row][col+1] 
                    mc = grid[row+1][col] 
                    lr = grid[row+2][col-1] + grid[row+2][col] + grid[row+2][col+1] 
                    curr_sum = ur+mc+lr
                    max_sum = max(max_sum, curr_sum)
        
        return max_sum
                
