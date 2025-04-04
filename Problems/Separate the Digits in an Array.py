class Solution:
    def separateDigits(self, nums: list[int]) -> list[int]:
        result = []
        
        for num in nums:
            digits = list(map(int, str(num)))
            result.extend(digits)
        
        return result
