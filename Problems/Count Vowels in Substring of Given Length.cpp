class Solution {
public:
    int maxVowels(string s, int k) {
        auto isVowel = [](char c) {
            return c == 'a' || c == 'e' || c == 'i' || c == 'o' || c == 'u';
        };

        int count = 0, maxCount = 0;
        for (int i = 0; i < s.size(); ++i) {
            if (isVowel(s[i])) count++;
            if (i >= k && isVowel(s[i - k])) count--;
            maxCount = max(maxCount, count);
        }

        return maxCount;
    }
};

