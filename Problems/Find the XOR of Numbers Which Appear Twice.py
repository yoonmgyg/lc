class Solution:
    def duplicateNumbersXOR(self, nums: List[int]) -> int:
        ans, seen = 0, set()
        for num in nums:
            if num in seen: ans^= num
            else: seen.add(num)  

        return ans
