class Solution:
    def transformArray(self, nums: List[int]) -> List[int]:
        zero_count = 0
        one_count = 0
        for i in range(len(nums)):
            if nums[i] % 2 == 0:
               zero_count+=1 
            else:
                one_count+=1    
        return [0] * zero_count + [1] * one_count  
