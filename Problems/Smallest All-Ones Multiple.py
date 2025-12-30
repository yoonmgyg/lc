class Solution:
    def minAllOneMultiple(self, k: int) -> int:
        if k % 2 == 0 or k % 5 == 0: return -1
        rem = 0
        for i in range(k):
            rem = (rem * 10 + 1) % k
            if rem == 0: return i + 1
        return -1
