# Create frequency of each char and check that there is no 0 in list
class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        lst = [0] * 26
        for i in sentence:
            lst[ord(i) - ord('a')] += 1
        return 0 not in lst
