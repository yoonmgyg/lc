class Solution:
    def hasSameDigits(self, s: str) -> bool:
        while len(s) > 2:
            s = "".join(str((int(s[i]) + int(s[i+1])) % 10) for i in range(len(s) - 1))
        return s[0] == s[1]
