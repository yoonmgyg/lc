class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        count = Counter(text)
        word = Counter('balloon')
        res = len(text)
        for i in word:
            res = min(res, count[i]//word[i])
        return res
