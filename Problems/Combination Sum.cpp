class Solution {
public:
    vector<vector<int>> combinationSum(vector<int>& candidates, int target) {
        vector<vector<int>> result;
        vector<int> current;

        function<void(int, int)> dfs = [&](int index, int remaining) {
            if (remaining == 0) {
                result.push_back(current);
                return;
            }
            if (index == candidates.size() || remaining < 0) return;

            // Include current number
            current.push_back(candidates[index]);
            dfs(index, remaining - candidates[index]);
            current.pop_back();

            // Skip to next number
            dfs(index + 1, remaining);
        };

        dfs(0, target);
        return result;
    }
};
