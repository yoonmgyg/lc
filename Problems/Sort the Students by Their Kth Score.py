# Sorts students by adding to dict and sorting keys in reverse
class Solution:
    def sortTheStudents(self, score: List[List[int]], k: int) -> List[List[int]]:
        d = {}
        for i in score:
            d[i[k]] = i
        keys = list(d.keys())
        keys.sort(reverse=True)
        return [d[i] for i in keys]
