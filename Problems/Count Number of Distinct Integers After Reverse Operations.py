class Solution(object):
    def countDistinctIntegers(self, nums):
        nums_set = set(nums)
        for num in nums:
            reverse_num = int(str(num)[::-1])
            nums_set.add(reverse_num)
        return len(nums_set)
