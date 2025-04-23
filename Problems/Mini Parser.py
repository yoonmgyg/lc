class Solution:
    def deserialize(self, s: str) -> NestedInteger:
        if not s: 
            return NestedInteger()
        if not s.startswith("["): 
            return NestedInteger(int(s)) 
        ans = NestedInteger()
        s = s[1:-1]
        if s: 
            ii = op = 0 
            for i in range(len(s)): 
                if s[i] == "[": op += 1
                if s[i] == "]": op -= 1
                if s[i] == "," and op == 0: 
                    ans.add(self.deserialize(s[ii:i]))
                    ii = i+1
            ans.add(self.deserialize(s[ii:i+1]))
        return ans 
