class Solution:
    def escapeGhosts(self, ghosts: List[List[int]], target: List[int]) -> bool:
        xx, yy = target 
        return all(abs(x-xx) + abs(y-yy) > abs(xx) + abs(yy) for x, y in ghosts)
