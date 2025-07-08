class Solution {
public:
    vector<int> minBitwiseArray(vector<int>& nums) {
        vector<int> ans;

        for (auto& num : nums) {
            if (num == 2) {
                ans.push_back(-1);
            } 
            else {
                for (char i = 10; i >= 0; i--) {
                    if((num & (1 << i)) != 0){
                        int temp = num & ~(1 << i);
                        if((temp++ | temp) == num){
                            ans.push_back(temp - 1);
                            break;
                        }
                    }
                }
            }
        }

        return ans;
    }
};
