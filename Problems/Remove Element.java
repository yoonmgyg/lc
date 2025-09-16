class Solution {
    public int removeElement(int[] nums, int val) {
        int i = 0;
        int res = 0;
        int right = nums.length - 1;
        while (i <= right) {
            if (nums[i] == val) {
                nums[i] = nums[right];
                right--; 
            } else {
                ++res;
                ++i;
            }
        }

        return res;
    }
}
