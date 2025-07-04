class Solution {
public:
    int lengthOfLongestSubstring(string s) {
        unordered_map<char, int> state;
        int start = 0;
        int res = 0;

        for (int end = 0; end < s.length(); ++end) {
            ++state[s[end]];

            while (state[s[end]] > 1) {
                --state[s[start]];
                ++start;
            }
            res = max(res, end - start + 1);
        }
        return res;
    }
};
