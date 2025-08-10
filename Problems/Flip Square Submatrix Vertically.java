class Solution {
    public int[][] reverseSubmatrix(int[][] grid, int x, int y, int k) {
            for (int i = 0; i < k; ++i) {
                for (int j = 0; j < k / 2; ++j) {
                    int tmp = grid[x + j][y + i]; // start at top of submatrix
                    grid[x + j][y + i] = grid[x + k - 1 - j][y + i];  // assign bottom of submatrix to top
                    grid[x + k - 1 - j][y + i] = tmp; // assign top to bottom
            } 
        }
        return grid;
    }
}
