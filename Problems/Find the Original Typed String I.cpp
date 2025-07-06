class Solution {
public:
    int possibleStringCount(string word) {
        long long ans = 1;                         
        for (int i = 0, n = word.size(); i < n; ) {
            int j = i;
            while (j < n && word[j] == word[i]) ++j; 
            ans += (j - i - 1);                    
            i = j;
        }
        return static_cast<int>(ans);
    }
};
