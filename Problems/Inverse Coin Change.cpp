typedef long long ll;
class Solution {
public:
    vector<int> findCoins(vector<int>& nums) {
        int n = nums.size();
        vector<ll> ways(n + 1, 0);
        ways[0] = 1;
        vector<int> coins;

        for (int a = 1; a <= n; a++) {
            ll want = nums[a - 1];
            ll have = ways[a];
            ll dif = want - have;

            if (have > want) return {};
            if (have == want) continue;
            if (dif != 1) return {};

            coins.push_back(a);
            for (int j = a; j <= n; j++) {
                ways[j] += ways[j - a];
            }
        }

        return coins;
    }
};
