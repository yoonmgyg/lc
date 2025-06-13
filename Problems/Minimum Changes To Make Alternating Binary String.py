class Solution:
    def minOperations(self, s: str) -> int:
        start10 = 0
        for i, c in enumerate(s):
            if int(c) == i % 2:
                start10 += 1

        return min(start10, len(s) - start10)
