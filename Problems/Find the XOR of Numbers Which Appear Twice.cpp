class Solution {
private:
    bool arr[51];
public:
    int duplicateNumbersXOR(vector<int>& nums) {
        int _xor = 0;
        for (auto& i : nums){
            if (arr[i]){
                _xor ^= i;
            }
            arr[i] = true;
        }

        return _xor;
    }
};
