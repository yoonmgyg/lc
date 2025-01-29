# Finds unique binary string by using greedy algorithm to append opposite value from current index
class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        res = []
        for i in range(len(nums)):
            if nums[i][i] == '1':
                res.append('0')
            else:
                res.append('1')
        return "".join(res)
