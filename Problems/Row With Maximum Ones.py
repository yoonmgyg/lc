class Solution:
    def rowAndMaximumOnes(self, mat: List[List[int]]) -> List[int]:
        indexes = [i.count(1) for i in mat]
        return [indexes.index(max(indexes)), max(indexes)]
