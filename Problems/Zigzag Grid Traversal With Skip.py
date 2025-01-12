# Gets dimensions of grid and loops through, going left to right if even and right to left if not
class Solution:
    def zigzagTraversal(self, grid: List[List[int]]) -> List[int]:
        m, n = len(grid), len(grid[0]) 
        result = []
        
        for i in range(m):
            if i % 2 == 0: 
                row = grid[i][::2]  
            else:  
                row = grid[i][::-1][n % 2::2]  
            result.extend(row)
        
        return result
