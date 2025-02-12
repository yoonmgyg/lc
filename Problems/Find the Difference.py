# Count freq in dict and then get remaining chars when subtracting
class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        count = {}

        for c in t:
            count[c] = count.get(c, 0) + 1

        for c in s:
            count[c] -= 1
            if count[c] == 0:
                del count[c]

        # The remaining character in the dictionary is the difference
        return list(count.keys())[0]
