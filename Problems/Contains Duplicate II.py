class Solution:
    def containsNearbyDuplicate(self, nums: list[int], k: int) -> bool:
        index_map = {}  
        
        for i, num in enumerate(nums):
            if num in index_map and abs(i - index_map[num]) <= k:
                return True
            index_map[num] = i  
        
        return False
