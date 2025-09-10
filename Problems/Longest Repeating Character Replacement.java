class Solution {
    public int characterReplacement(String s, int k) {
        Map<Character, Integer> freq = new HashMap<>();
        int res = 0;
        int max_freq = 0;
        int l = 0;
        for (int r = 0; r < s.length(); ++r) {
            char ch = s.charAt(r);
            freq.merge(ch, 1, Integer::sum);
            max_freq = Math.max(max_freq, freq.get(ch));
            while (r - l + 1 > max_freq + k) {
                char leftCh = s.charAt(l);
                freq.put(leftCh, freq.get(leftCh) - 1);
                ++l;
            }

            res = Math.max(res, r - l + 1);
        }

        return res;
    }
}
