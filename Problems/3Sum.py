# Gets the sum of 3 number through 2 pointers looping across sorted list
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i-1]:
                i += 1

            j = i + 1
            k = len(nums) - 1
            while j < k:
                add = nums[i] + nums[j] + nums[k]
                if add > 0:
                    k -= 1
                elif add < 0:
                    j += 1
                else:
                    res.append([nums[i], nums[j], nums[k]])
                    j += 1
                    while nums[j] == nums[j-1] and j < k:
                        j += 1
            
            return res
                    
