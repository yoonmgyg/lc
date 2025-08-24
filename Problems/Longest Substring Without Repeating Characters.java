class Solution {
    public int lengthOfLongestSubstring(String s) {
        Map<Character, Integer> map = new HashMap<>();
        int left = 0, maxLen = 0;

        for (int right = 0; right < s.length(); right++) {
            char c = s.charAt(right);
            if (map.containsKey(c) && map.get(c) >= left) {
                left = map.get(c) + 1; // move left past duplicate
            }
            map.put(c, right); // record last index
            maxLen = Math.max(maxLen, right - left + 1); // update answer
        }
        return maxLen;
    }
}
