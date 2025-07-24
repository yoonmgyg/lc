class Solution {
public:
    vector<int> topKFrequent(vector<int>& nums, int k) {
        unordered_map<int, int> freq;
        for (int num : nums) freq[num]++;

        priority_queue<pair<int, int>> pq;
        for (auto& [num, count] : freq) {
            pq.push({count, num});
        }

        vector<int> result;
        while (k-- > 0 && !pq.empty()) {
            result.push_back(pq.top().second);
            pq.pop();
        }

        return result;
    }
};
