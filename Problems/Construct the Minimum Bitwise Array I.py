class Solution:
    def minBitwiseArray(self, nums):
        def helper(num):
            if  num % 4 == 1:           
                return num - 1 
            if num % 4 == 3:         
                tmp = num
                for i in range(num.bit_length()):
                    tmp //= 2
                    if not tmp % 2:
                        break
                return num - (1<<i)     
            return -1                   
        return map(helper,nums)
