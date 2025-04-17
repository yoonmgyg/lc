class Solution:
    def evenOddBit(self, n: int) -> List[int]:
        res = [0, 0]
        i = 0
        while n > 0:
            if n & 1:
                res[i % 2] += 1
            n >>= 1
            i += 1
        return res

