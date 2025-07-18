class Solution {
public:
    vector<vector<int>> minAbsDiff(vector<vector<int>>& grid, int k) {
        vector<vector<int>> ans;
        int r = grid.size(), c = grid[0].size();
        for (int i = 0; i <= r - k; i++) {
            ans.push_back({});
            for (int j = 0; j <= c - k; j++) {
                vector<int> arr;
                for (int x = i; x < i + k; x++) {
                    for (int y = j; y < j + k; y++) {
                        arr.push_back(grid[x][y]);
                    }
                }
                int minDiff = INT_MAX;
                sort(arr.begin(), arr.end());
                for (int idx = 0; idx < arr.size() - 1; idx++) {
                    if (arr[idx + 1] == arr[idx])
                        continue;
                    int diff = arr[idx + 1] - arr[idx];
                    if (diff < minDiff)
                        minDiff = diff;
                }
                ans.back().push_back(minDiff == INT_MAX ? 0 : minDiff);
            }
        }
        return ans;
    }
};
