class Solution:
    def minMaxGame(self, nums: List[int]) -> int:
        def minmax(lis):
            final = []
            count = 1
            for i in range(0,len(lis),2):
                temp = lis[i:i+2]
                if count%2 !=0:
                    final.append(min(temp))
                else:
                    final.append(max(temp)) 
                count+=1
            return final
        while(len(nums)!=1):
            nums = minmax(nums)
        return nums[0]
        
