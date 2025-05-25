class Solution:
    def minSteps(self, s: str, t: str) -> int:
        fs, ft = Counter(s), Counter(t)
        return sum((fs-ft).values()) + sum((ft-fs).values())
