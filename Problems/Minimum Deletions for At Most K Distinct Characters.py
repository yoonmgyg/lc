class Solution:
    def minDeletion(self, s: str, k: int) -> int:
        
        ctr = defaultdict(int)
        for ch in s: ctr[ch]+= 1

        return sum(nsmallest(len(ctr) - k, ctr.values()))
