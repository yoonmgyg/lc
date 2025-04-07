class Solution:
    def countKeyChanges(self, s: str) -> int:
        n = len(s)
        c = 0
        for i in range(1, n):
            if (ord(s[i]) - ord('a') == ord(s[i - 1]) - ord('A')) or (ord(s[i]) - ord('A') == ord(s[i - 1]) - ord('a')) or s[i] == s[i - 1]:
                c += 1
        return n - 1 - c
