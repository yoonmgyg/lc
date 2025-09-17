class Solution {
    public boolean[] subsequenceSumAfterCapping(int[] nums, int k) {
        int n = nums.length;
        boolean[] res = new boolean[nums.length];
        for (int x = 1; x <= n; ++x) {
            int[] capped = new int[n];
            for (int i = 0; i < n; ++i) {
                capped[i] = Math.min(x, nums[i]);
            }

            boolean[] dp = new boolean[k + 1];
            dp[0] = true;
            for (int num : capped) {
                for (int sum = k; sum >= num; --sum) {
                    dp[sum] = dp[sum] || dp[sum - num];
                }
            }
            res[x-1] = dp[k];
        }
        return res;
    }
}
