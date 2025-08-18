class Solution {
    public int coinChange(int[] coins, int amount) {
        int[] dp = new int[amount + 1];
        Arrays.fill(dp, amount + 1); // fill with large value
        dp[0] = 0; // base case: 0 coins to make 0

        for (int coin : coins) {
            for (int i = coin; i <= amount; i++) {
                dp[i] = Math.min(dp[i], dp[i - coin] + 1); // choose coin
            }
        }

        return dp[amount] > amount ? -1 : dp[amount]; // check if possible
    }
}
