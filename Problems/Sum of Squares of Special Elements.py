# Gets special elements by adding if i + 1 is divisible
class Solution:
    def sumOfSquares(self, nums: List[int]) -> int:
        count = 0
        n = len(nums) 
        for i in range(0,n) :
            if  n % (i+1) == 0:
                count += nums[i] ** 2
        return count
