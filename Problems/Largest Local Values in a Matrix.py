class Solution:
    def largestLocal(self, grid: List[List[int]]) -> List[List[int]]:
        n = len(grid)  # get the size of the grid
        maxLocal = []  # initialize the result matrix
        for i in range(n - 2):  # iterate over valid starting rows for 3x3 submatrices
            row = []  # list to store max values for the current row
            for j in range(n - 2):  # iterate over valid starting columns for 3x3 submatrices
                # find the maximum value in the 3x3 submatrix starting at (i, j)
                current_max = max(grid[x][y] for x in range(i, i + 3) for y in range(j, j + 3))
                row.append(current_max)  # add the maximum to the current row
            maxLocal.append(row)  # append the row to the result matrix
        return maxLocal
