class Solution:
    def minimumChairs(self, s: str) -> int:
        ma = 0
        curr = 0
        for i in s:
            if i == 'E':
                curr += 1
                ma = max(ma, curr)
            else:
                curr -= 1
        return ma
