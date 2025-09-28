class Solution:
    def evenNumberBitwiseORs(self, nums: List[int]) -> int:
        bit_ors = 0
        for num in nums:
            if (num % 2 == 0):
                bit_ors |= num
            
        return bit_ors
