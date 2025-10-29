class Solution:
    def minBitwiseArray(self, nums: List[int]) -> List[int]:
        def helper(num: int) -> int:
            if num == 2: return -1
            bin_arr = [0] + list(map(int, bin(num)[2:]))
            for i in range(len(bin_arr) - 1, -1, -1):
                if bin_arr[i] == 0:
                    bin_arr[i + 1] = 0
                    break
            res = power = 0
            for i in range(len(bin_arr) - 1, -1, -1):
                res += bin_arr[i] * (2 ** power)
                res + bin_arr[i]
                power += 1
            return res
        
        return [helper(num) for num in nums]
