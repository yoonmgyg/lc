class Solution {
    public int removeDuplicates(int[] nums) {
        int left = 0;
        int k = 0;
        int prev = 101;
        for (int i = 0; i < nums.length; ++i) {
            if (nums[i] != prev) {
                prev = nums[i];
                nums[left] = nums[i];
                ++left;
            }
        }
        return left;
    }
}
