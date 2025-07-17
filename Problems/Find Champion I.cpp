class Solution {
public:
    int findChampion(vector<vector<int>>& grid) {
        int n = grid.size(), champ = 0, col = 0;
        while (++col < n){
            if (grid[champ][col] == 0) champ = col;
        }
        return champ;
    }
};
