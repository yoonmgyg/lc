class Solution:
    def deserialize(self, s: str) -> NestedInteger:
        return self._deserialize(s, 0, len(s) - 1)

    def _deserialize(self, s: str, i, j) -> NestedInteger:
        if s[i] != "[":  
            return NestedInteger(int(s[i:j+1]))

        res = NestedInteger()
        if j == i + 1: 
            return res

        start = idx = i + 1  
        count = 0 
        while idx <= j:
            if count == 0 and (s[idx] == "," or s[idx] == "]"):  
                res.add(self._deserialize(s, start, idx - 1))  
                start = idx + 1
            elif s[idx] == "[":  
                count += 1
            elif s[idx] == "]":
                count -= 1
            idx += 1
        return res
