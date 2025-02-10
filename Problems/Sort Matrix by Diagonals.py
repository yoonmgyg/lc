class Solution:
    def sortMatrix(self, grid: List[List[int]]) -> List[List[int]]:
        n = len(grid)
        
        for row in range(n):
            i, j = row, 0
            diagonal = []
            coords = []
            while i < n and j < n:
                diagonal.append(grid[i][j])
                coords.append((i, j))
                i += 1
                j += 1
            diagonal.sort(reverse=True)
            for (i, j), value in zip(coords, diagonal):
                grid[i][j] = value
    
        for col in range(1, n):
            i, j = 0, col
            diagonal = []
            coords = []
            while i < n and j < n:
                diagonal.append(grid[i][j])
                coords.append((i, j))
                i += 1
                j += 1
            diagonal.sort()
    
            for (i, j), value in zip(coords, diagonal):
                grid[i][j] = value
    
        return grid
