# Adds number of pairs by getting unique elements and adding any evens and odds to output
class Solution:
    def numberOfPairs(self, nums: List[int]) -> List[int]: 
            output = []  
            pair = 0
            unique = list(set(nums))
            for i in range(len(unique)):
                count = nums.count(unique[i]) 
                if count % 2 != 0:
                    output.append(unique[i]) 
                pair += (count) // 2 
            return [pair, len(output)] 
