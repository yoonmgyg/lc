# get max and min values with k, then return range
class Solution:
    def smallestRangeI(self, nums: List[int], k: int) -> int:
        if not k and len(nums)==1:
            return 0
        mi = min(nums) + k
        mx = max(nums)- k
        if mi > mx:
            return 0
        else:
            return mx - mi
