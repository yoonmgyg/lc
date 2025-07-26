class Solution {
public:
    int leastInterval(vector<char>& tasks, int n) {
        vector<int> freq(26, 0);
        for (char t : tasks) freq[t - 'A']++;

        sort(freq.begin(), freq.end());
        int maxFreq = freq[25] - 1;
        int idleSlots = maxFreq * n;

        for (int i = 24; i >= 0 && freq[i] > 0; --i) {
            idleSlots -= min(freq[i], maxFreq);
        }

        return idleSlots > 0 ? tasks.size() + idleSlots : tasks.size();
    }
};
