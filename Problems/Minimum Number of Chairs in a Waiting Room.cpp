class Solution {
public:
    int minimumChairs(string s) {
        int min = 0, temp = 0;
        for(int i = 0, n = s.length(); i < n; ++i){
            temp += (s[i] == 'E') ? 1 : -1;
            if(temp > min) min = temp;
        }
        return min;
    }
};
