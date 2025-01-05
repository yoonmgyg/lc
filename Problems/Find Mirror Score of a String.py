# Creates a dict to map chars and gets mirrored chars by subtracting the ord of a, then uses 25 - charIndex to get the equivalent char in the dict
class Solution:
    def calculateScore(self, s: str) -> int:
        d = defaultdict(list)
        ans = 0
        for i, c in enumerate(s):
            charIndex = ord(c) - ord('a')
            key = 25 - charIndex
            if d[key]:
                ans += (i-d[key].pop())
            else:
                d[charIndex].append(i)
        return ans
                
