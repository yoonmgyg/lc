class Solution:
    def findColumnWidth(self, grid: List[List[int]]) -> List[int]:
        col = len(grid[0])
        res = []
        for i in range(col):
            temp = []
            for row in grid:
                temp.append(len(str(row[i])))
            res.append(max(temp))
        return res
