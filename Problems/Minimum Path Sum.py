class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        x = len(grid)
        y = len(grid[0])
        small = [float('inf') for _ in range(y)]
        small[0] = 0
        for row in grid:
            small[0] += row[0]
            for i in range(1,len(small)):
                if small[i-1] < small[i]: small[i] = small[i-1] + row[i]
                else: small[i] += row[i]
        return small[-1]
