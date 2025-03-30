class Solution:
    def reverseDegree(self, s: str) -> int:
        i = 1
        result = 0
        z_ascii =  ord('z')
        for c in s:
            result += (z_ascii - ord(c) + 1) * i
            i += 1
        return result
