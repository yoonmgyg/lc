class Solution:
    def wordBreak(s, wordDict):
      wordSet = set(wordDict)
      dp = [False] * (len(s) + 1)
      dp[0] = True # Empty string is a valid break
    
      for i in range(1, len(s) + 1):
        for j in range(i):
          sub = s[j:i]
          if dp[j] and sub in wordSet:
            dp[i] = True
            break
    
      return dp[len(s)]
