# Gets the score after flipping matrix by flipping if row has 0 and column has more 0s, then calculating sum
class Solution:
    def matrixScore(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
      
        for i in range(m):
            if grid[i][0] == 0:  
                for j in range(n):
                    grid[i][j] = 1 - grid[i][j]  # Toggle the values
        
        for j in range(1, n):
            count_ones = sum(grid[i][j] for i in range(m))
            if count_ones < m / 2: 
                for i in range(m):
                    grid[i][j] = 1 - grid[i][j]  # Toggle the values
        
        score = 0
        for i in range(m):
            binary_str = ''.join(map(str, grid[i])) 
            score += int(binary_str, 2) 
        
        return score
