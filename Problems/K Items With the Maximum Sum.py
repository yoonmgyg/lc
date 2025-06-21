class Solution:
    def kItemsWithMaximumSum(self, numOnes: int, numZeros: int, numNegOnes: int, k: int) -> int:
        nums = [1] * numOnes + [0] * numZeros + [-1] * numNegOnes
        return reduce(lambda x, y : x + y, nums[:k], 0)
