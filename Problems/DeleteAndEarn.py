class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        if not nums : return 0
        house = [0] * (max(nums)+1)
        for num in nums:
            house[num] += num
        
        dp = [0]*(len(house)+1)
        for i in range(1,len(house)):
            dp[i] = max(house[i]+dp[i-2], dp[i-1])
        return max(dp[-1],dp[-2])
