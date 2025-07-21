class Solution {
public:
    vector<int> sortedSquares(vector<int>& nums) {
        int n = nums.size();
        vector<int> res(n);
        int left = 0, right = n - 1, pos = n - 1;
        while (left <= right) {
            if (abs(nums[left]) > abs(nums[right])) {
                res[pos--] = nums[left] * nums[left++];
            } else {
                res[pos--] = nums[right] * nums[right--];
            }
        }
        return res;
    }
};
