class NeighborSum:

    def __init__(self, grid: List[List[int]]):
        self.grid = grid
        self.size = len(grid)
        self.positions = [None] * self.size ** 2
        
        for i, j in product(range(self.size), range(self.size)):
            self.positions[grid[i][j]] = i, j

    def adjacentSum(self, value: int) -> int:
        i, j = self.positions[value]
        sm = 0
        sm += self.grid[i-1][j] if i >= 1 else 0 
        sm += self.grid[i+1][j] if i+1 < self.size else 0
        sm += self.grid[i][j-1] if j >= 1 else 0 
        sm += self.grid[i][j+1] if j+1 < self.size else 0

        return sm

    
    def diagonalSum(self, value: int) -> int:
        i, j = self.positions[value]
        sm = 0
        sm += self.grid[i-1][j-1] if i >= 1 and j >= 1 else 0
        sm += self.grid[i+1][j+1] if i+1 < self.size and j+1 < self.size else 0
        sm += self.grid[i-1][j+1] if i >= 1 and j+1 < self.size else 0 
        sm += self.grid[i+1][j-1] if i+1 < self.size and j >= 1 else 0

        return sm
