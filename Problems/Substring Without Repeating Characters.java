class Solution {
    public int lengthOfLongestSubstring(String s) {
        Set<Character> state = new HashSet<>();
        int res = 0;

        int left = 0;
        for (int right = 0; right < s.length(); ++right) {
            while (state.contains(s.charAt(right))) {
                state.remove(s.charAt(left));
                ++left;
            }
            state.add(s.charAt(right));
            res = Math.max(res, right - left + 1);
        }

        return res;
    }
}
