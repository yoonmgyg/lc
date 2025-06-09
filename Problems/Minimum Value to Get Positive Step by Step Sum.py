class Solution:
    def minStartValue(self, nums: List[int]) -> int:
        prefixSum = 0
        minVal = float('inf')
        for n in nums:
            prefixSum += n
            minVal = min(prefixSum,minVal)

        if minVal < 0:
            return -(minVal) +1
        return 1
        
