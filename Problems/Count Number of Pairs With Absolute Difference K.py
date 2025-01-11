# Use dict to count frequency of number and return number of pairs with k
class Solution:
    def countKDifference(self, nums: List[int], k: int) -> int:
        count = 0
        hash = {}
        
        for i in nums:
            if i in hash:
                hash[i] += 1
            else:
                hash[i] = 1
                
        for i in hash:
            if i+k in hash:
                count += hash[i] * hash[i+k]
                
        return count
