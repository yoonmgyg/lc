class Solution {
    public int[] dailyTemperatures(int[] temps) {
        int n = temps.length;
        int[] res = new int[n];
        Deque<Integer> stack = new ArrayDeque<>(); // store indices

        for (int i = 0; i < n; i++) {
            while (!stack.isEmpty() && temps[i] > temps[stack.peek()]) {
                int prev = stack.pop();
                res[prev] = i - prev; // days until warmer temp
            }
            stack.push(i); // add current index
        }

        return res;
    }
}
