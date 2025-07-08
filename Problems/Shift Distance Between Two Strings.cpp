class Solution {
public:
    long long shiftDistance(string s, string t, vector<int>& nextCost, vector<int>& preCost) {
        vector<long long> next(26);
        vector<long long> pre(26);

        long long ans = 0;
        next[0] = nextCost[25];
        pre[25] = preCost[0];
        int dec = 25;
        for (int i = 1; i < 26; ++i) {
            next[i] = next[i-1] + nextCost[i-1];
            pre[25-i] = pre[25-i+1] + preCost[25-i+1];
        }
        int n = s.size();
        for(int i = 0; i < n; ++i){
            int si = s[i]-'a';
            int ti = t[i]-'a';
            if(si < ti){
                ans += min(next[ti]-next[si],pre[0]+pre[ti]-pre[si]);
            }
            else{
                ans += min(pre[ti]-pre[si],next[25]+next[ti]-next[si]);
            }
        }
        return ans;
    }
};
