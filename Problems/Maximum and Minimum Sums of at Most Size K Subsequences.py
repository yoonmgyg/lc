# get combinations of each number to get min and max numbers and modulo to get results
class Solution:
    def minMaxSums(self, nums: List[int], k: int) -> int:
        res = 0
        n = len(nums)
        nums.sort()

        for i in range(n):
            for j in range(1, min(k, i + 1) + 1):
                res += nums[i] * math.comb(i, j - 1)  
                
            for j in range(1, min(k, n - i) + 1):
                res += nums[i] * math.comb(n - i - 1, j - 1)  
        
        return res % (10 ** 9 + 7)