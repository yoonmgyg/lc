class Solution:
    def longestBalanced(self, nums: List[int]) -> int:
        longest = 0 
        for i in range(len(nums)):
            count = 0 
            even_set, odd_set = set(), set()
            for j in range(i, len(nums)):
                if nums[j] % 2 == 0:
                    even_set.add(nums[j])
                else:
                    odd_set.add(nums[j])
                count += 1
                if len(even_set) == len(odd_set):
                    longest = max(longest, count)

                # early termination: if we can't beat current max, stop
                if len(nums) - i <= longest:
                    break
        return longest 
