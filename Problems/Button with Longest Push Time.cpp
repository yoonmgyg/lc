class Solution {
public:
    int buttonWithLongestTime(vector<vector<int>>& events) {
        int maxi = events[0][0], maxdur = events[0][1];
        for(int i = 1, n = events.size(); i < n; ++i){
            int idx = events[i][0], dur = events[i][1] - events[i - 1][1];
            if(dur > maxdur){
                maxdur = dur;
                maxi = idx;
            }
            else if(dur == maxdur) maxi = min(maxi , idx);
        }
        return maxi;
    }
};
