class Solution:
    def pacific_atlantic_flow(self, grid: List[List[int]]):
        if not grid or not grid[0]:
            return []
        dp_pac = [[False] * len(grid[0]) for i in range(len(grid))]
        dp_atl = [[False] * len(grid[0]) for i in range(len(grid))]
        dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        def dfs(r, c, seen):
            if seen[r][c]:
                return
            
            seen[r][c] = True
            
            for dr, dc in dirs:
                nr, nc = r + dr, c + dc
                if (0 <= nr < len(grid) and 0 <= nc < len(grid[0]) and
                grid[nr][nc] >= grid[r][c]):
                    dfs(nr, nc, seen)

        for i in range(len(grid)):
            dfs(i, 0, dp_pac)
        for i in range(len(grid[0])):
            dfs(0, i, dp_pac)

        for i in range(len(grid[0])):
            dfs(len(grid)-1, i, dp_atl)
        for i in range(len(grid)):
            dfs(i, len(grid[0])-1, dp_atl)



        res = []
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if dp_pac[i][j] and dp_atl[i][j]:
                    res.append([i, j])
        
        return res
            
