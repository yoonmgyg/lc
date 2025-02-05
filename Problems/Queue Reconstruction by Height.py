# Sorts h by decreasing and k by increasing to reconstruct queue
class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        result = []
        for h, k in sorted(people, key=lambda x: (-x[0], x[1])):
            result.insert(k, [h, k])
        return result
