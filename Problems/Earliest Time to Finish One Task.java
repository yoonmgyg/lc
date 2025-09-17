class Solution {
    public int earliestTime(int[][] tasks) {
        int res = Integer.MAX_VALUE;
        for (int i = 0; i < tasks.length; ++i) {
            res = Math.min(res, tasks[i][0] + tasks[i][1]);
        }
        return res;
    }
}
