# Loops through grid and adds the difference between each element as an operation
class Solution:
    def minimumOperations(self, grid: List[List[int]]) -> int:
        res = 0
        for i in range(len(grid[0])):
            for j in range(1, len(grid)):
                if grid[j][i] <= grid[j-1][i] + 1:
                    res += grid[j-1][i] + 1 - grid[j][i]
                    grid[j][i] = grid[j-1][i] + 1
                    
        return ops
