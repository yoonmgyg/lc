class Solution:
    def baseUnitConversions(self, conv: List[List[int]]) -> List[int]:
        mod = 100_000_0007
        res = [1]*(len(conv)+1)
        for a in conv:
            res[a[1]] = (res[a[0]] * a[2]) % mod

        return res
        
