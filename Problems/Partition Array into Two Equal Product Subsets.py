class Solution:
    def checkEqualPartitions(self, nums: List[int], target: int) -> bool:
        n = len(nums)
        total_subsets = 1 << n 
    
        for mask in range(1, total_subsets - 1): 
            subset = []
            complement = []
            prod1 = 1
            prod2 = 1
            for i in range(n):
                if mask & (1 << i):
                    subset.append(nums[i])
                    prod1 *= nums[i]
                else:
                    complement.append(nums[i])
                    prod2 *= nums[i]
            
            if prod1 == target and prod2 == target:
                return True
        return False
