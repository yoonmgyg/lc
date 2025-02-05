# Loop through index and distribute based on largest values
class Solution:
    def resultArray(self, nums):
        len_nums = len(nums)
        
        arr1 = [nums[0]]
        arr2 = [nums[1]]

        i = 2
        while (i < len_nums):
            if (arr1[-1] > arr2[-1]):
                arr1.append(nums[i])
            else:
                arr2.append(nums[i])
            
            i += 1

        return arr1 + arr2
