class Solution {
    public int sortPermutation(int[] nums) {
        int n = nums.length;
        boolean sorted = true;
        for (int i = 0; i < n; ++i) { // check for sort
            if (nums[i] != i) { sorted = false; break; }
        }
        if (sorted) return 0;

        int k = -1;
        for (int i = 0; i < n; ++i) { // get AND values and get permutations
            if (nums[i] != i) {
                k &= i;
                k &= nums[i];
            }
        }
        return k;
    }
}
