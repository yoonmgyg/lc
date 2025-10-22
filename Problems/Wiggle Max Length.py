
class Solution:
    def wiggleMaxLength(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 0:
            return 0
        
        last_increase = [0] * n
        last_decrease = [0] * n
        
        last_increase[0] = 1
        last_decrease[0] = 1
        res = 1
        
        for i in range(1, n):
            last_increase[i] = 1
            last_decrease[i] = 1
            
            for j in range(i):
                if nums[i] > nums[j]:
                    last_increase[i] = max(last_increase[i], last_decrease[j] + 1)
                elif nums[i] < nums[j]:
                    last_decrease[i] = max(last_decrease[i], last_increase[j] + 1)
            
            res = max(res, max(last_increase[i], last_decrease[i]))
        
        return res
