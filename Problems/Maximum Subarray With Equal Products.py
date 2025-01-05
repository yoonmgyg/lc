# Gets array with equal products by getting the gcd and lcm of each array and seeing if the product equals the gcd * lcm
class Solution:
    def maxLength(self, nums: List[int]) -> int:
        res = 1
        for i in range(len(nums)):
            for j in range(i, len(nums)):
                arr = nums[i:j+1]
                gcd = reduce(math.gcd, arr)
                lcm = reduce(math.lcm, arr)
                product = math.prod(arr)
                if product == gcd * lcm:
                    res = max(len(arr),maxi)
        return res
