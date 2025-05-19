class Solution:
    def generateSubsets(self, index, ans, nums, subset):
        if index == len(nums):
            if subset not in ans: 
                ans.append(list(subset))
            return

        subset.append(nums[index])
        self.generateSubsets(index + 1, ans, nums, subset)

        subset.pop()
        self.generateSubsets(index + 1, ans, nums, subset)

    def subsetsWithDup(self, nums):
        ans = []
        nums.sort()  
        self.generateSubsets(0, ans, nums, [])
        return ans
