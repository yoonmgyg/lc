class Solution:
    MAX_TARGET = 1010  
    def __init__(self):
        self.dp = [-1] * Solution.MAX_TARGET  
    def countCombinations(self, nums, remainingTarget):
        if remainingTarget == 0:
            return 1
          
        if remainingTarget < 0:
            return 0
        
        if self.dp[remainingTarget] != -1:
            return self.dp[remainingTarget]
        
        currentCombinations = 0
        
        for currentNum in nums:
            currentCombinations += self.countCombinations(nums, remainingTarget - currentNum)
        
        self.dp[remainingTarget] = currentCombinations
        return currentCombinations

    def combinationSum4(self, nums, target):
        return self.countCombinations(nums, target)
