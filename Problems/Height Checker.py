# Sorts heights and loops through, checking if height matches sorted list
class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        k = sorted(heights)
        count = 0
		
        for i in range(len(heights)):
            if k[i] != heights[i]:
                count += 1
        return count
           
           
