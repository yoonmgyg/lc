class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
       
        max_candies = max(candies)
        result = []
        for i in candies:
                result.append(i + extraCandies >= max_candies)
        return result
