# Use set to get already seen numbers
class Solution:
    def getSneakyNumbers(self, nums: List[int]) -> List[int]:
        ans = []
        seen = set()
        for x in nums: 
            if x in seen: ans.append(x)
            else: seen.add(x)
        return ans 
