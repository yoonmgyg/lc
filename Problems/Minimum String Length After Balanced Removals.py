class Solution:
    def minLengthAfterRemovals(self, s: str) -> int:
        a = 0
        b = 0
        removed = 0
        for ch in s:
            if ch == 'a':
                a += 1
            elif ch == 'b':
                b += 1

            if a > 0 and b > 0:
                removed += 2
                a -= 1
                b -= 1
        return len(s) - removed
            
