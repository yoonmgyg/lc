class Solution:
    def sumDivisibleByK(self, nums: List[int], k: int) -> int:
        sum = 0
        freq = defaultdict(int)
        
        for num in nums:
            freq[num] += 1

        for num, count in freq.items():
            if count % k == 0:
                sum += num * count

        return sum
