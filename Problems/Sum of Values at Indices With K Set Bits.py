class Solution:
    def sumIndicesWithKSetBits(self, nums: List[int], k: int) -> int:
        sum = 0
        for i in range(len(nums)):
            bin_rep = bin(i)[2:]
            if bin_rep.count('1') == k:
                sum += nums[i]
        return sum
                
