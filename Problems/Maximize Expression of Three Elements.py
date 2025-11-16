class Solution:
    def maximizeExpressionOfThree(self, nums: List[int]) -> int:
        first = float('-inf')
        second = float('-inf')
        last = float('inf')
        for num in nums:
            if num > first:
                second = first
                first = num
            elif num > second:
                second = num
            if num < last:
                last = num

        return first + second - last
