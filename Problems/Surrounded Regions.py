class Solution:
    def surrounded_regions(self, grid: List[List[str]]):
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        visited = set()
        def dfs(r, c):
            if r < 0 or r >= len(grid) or c < 0 or c >= len(grid[0]) :
                return False
            if grid[r][c] == "X" or (r, c) in visited:
                return True
                        
            surrounded = True 
            visited.add((r, c))
            for dr, dc in directions:
                if not dfs(r + dr, c + dc):
                    surrounded = False
            
            if surrounded:
                grid[r][c] = "X"

            return surrounded
        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "O" and (i, j) not in visited:
                    dfs(i, j)
        
        return grid
