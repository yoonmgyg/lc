class Solution {
public:
    vector<vector<int>> permute(vector<int>& nums) {
        vector<vector<int>> result;
        vector<int> current = nums;

        function<void(int)> backtrack = [&](int start) {
            if (start == current.size()) {
                result.push_back(current);
                return;
            }
            for (int i = start; i < current.size(); ++i) {
                swap(current[start], current[i]);
                backtrack(start + 1);
                swap(current[start], current[i]);
            }
        };

        backtrack(0);
        return result;
    }
};
