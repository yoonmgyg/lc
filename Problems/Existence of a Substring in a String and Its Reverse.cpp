class Solution {
public:
    bool isSubstringPresent(string s) {
        string temp = s;
        reverse(begin(temp),end(temp));

        for (int i=0; i < s.length()-1; i++) {
            string sub=s.substr(i,2);
            if (temp.find(sub)!=string::npos) return true;
        }
        return false;
    }
};
