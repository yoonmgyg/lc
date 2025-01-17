# loop through each char in string and add if L, subtract if R and add to result if equal
class Solution:
    def balancedStringSplit(self, S: str) -> int:
        m = c = 0
        for s in S:
            if s == 'L': c += 1
            if s == 'R': c -= 1
            if c == 0: m += 1
        return m
