class Solution:
    def number_of_islands(self, grid: List[List[int]]):
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        visited = set()
        islands = 0
        def dfs(r, c):
            if (r < 0 or r >= len(grid) or c < 0 or c >= len(grid[0])
            or (r, c) in visited or grid[r][c] == 0):
                return
            
            visited.add((r, c))
            for dr, dc in directions:
                dfs(r + dr, c + dc)

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if (i, j) not in visited and grid[i][j] == 1:
                    dfs(i, j)
                    islands += 1

        return islands
