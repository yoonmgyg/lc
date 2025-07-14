class Solution {
public:
    bool isVowel(char a){
        return a == 'a' || a == 'e' || a == 'i' || a == 'o' || a == 'u';
    }

    int f(string word, int k) {
        if (k < 0) return 0;

        unordered_map<char, int> mp;
        int vCount = 0, totalVCount = 0;
        int i = 0, j = 0;
        int n = word.size();
        int res = 0;

        while (j < n) {
            if (isVowel(word[j])) {
                totalVCount++;
                if (mp.find(word[j]) != mp.end()) {
                    if (mp[word[j]] < i) {
                        vCount++;
                    }
                    mp[word[j]] = j;
                } else {
                    mp[word[j]] = j;
                    vCount++;
                }
            }

            while ((j - i + 1 - totalVCount) > k) {
                if (isVowel(word[i])) {
                    if (mp[word[i]] == i) vCount--;
                    totalVCount--;
                }
                i++;
            }

            if (vCount == 5) {
                int x = min({mp['a'], mp['e'], mp['i'], mp['o'], mp['u']});
                res += (x - i + 1);
            }
            j++;
        }

        return res;
    }

    int countOfSubstrings(string word, int k) {
        return f(word, k) - f(word, k - 1);
    }
};
