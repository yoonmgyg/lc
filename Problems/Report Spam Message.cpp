class Solution {
public:
    bool reportSpam(vector<string>& message, vector<string>& bannedWords) 
    {
        int cnt = 0;
        unordered_set<string>BanWords(begin(bannedWords), end(bannedWords));
        for (auto str : message) {
            cnt += BanWords.count(str);
            if (cnt == 2) return true;
        }
        return false;
    }
};
