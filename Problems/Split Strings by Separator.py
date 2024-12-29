# Splits each word by separator and adds to lis, then appends to ans
class Solution:
    def splitWordsBySeparator(self, words: List[str], separator: str) -> List[str]:
        lis = []
        ans = []
        for i in words:
            x = i.split(separator)
            if len(x) > 0:
                lis.extend(x)
        for i in lis:
            if len(i) > 0:
                ans.append(i)
        return ans
