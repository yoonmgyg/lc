class Solution:
    def isLongPressedName(self, name: str, typed: str) -> bool:
        t = len(typed);
        n = len(name);
        j = 0;
        i = 0;

        while j < t:
            if i < n and name[i] == typed[j]:
                i+=1;
                j+=1;
            elif i == 0 or name[i-1] != typed[j]:
                return False;
            else:
                j+=1

        return i >= n;
