class Solution {
    public List<List<Integer>> combinationSum(int[] candidates, int target) {
        Arrays.sort(candidates); // enable early stop
        List<List<Integer>> res = new ArrayList<>();
        dfs(candidates, 0, target, new ArrayList<>(), res);
        return res;
    }

    private void dfs(int[] nums, int start, int remain, List<Integer> path, List<List<Integer>> res) {
        if (remain == 0) {            // exact sum hit
            res.add(new ArrayList<>(path));
            return;
        }
        for (int i = start; i < nums.length; i++) {
            if (nums[i] > remain) break; // prune overshoot
            path.add(nums[i]);           // choose
            dfs(nums, i, remain - nums[i], path, res); // reuse allowed
            path.remove(path.size() - 1); // backtrack
        }
    }
}
