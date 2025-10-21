class Solution:
    def maxCount(self, m: int, n: int, ops: List[List[int]]) -> int:
        if len(ops) == 0:
            return m * n

        minimum_left = inf
        minimum_right = inf

        for a, b in ops:
            if a < minimum_left:
                minimum_left = a
            if b < minimum_right:
                minimum_right = b

        return minimum_left * minimum_right
