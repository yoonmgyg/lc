# Split words in paragraph and check if banned, then add to dict by freq
class Solution:
    def mostCommonWord(self, paragraph, banned):
        for c in "!?',;.": paragraph = paragraph.replace(c, " ")
        d, res, count = {},"",0
        for word in paragraph.lower().split():
            if word in banned:
                continue;
            elif word in d:
                d[word] += 1
            else:
                d[word] = 1
            if d[word] > count:
                count = d[word]
                res = word
        return res
