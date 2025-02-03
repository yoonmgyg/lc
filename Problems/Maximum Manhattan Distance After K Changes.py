# Loop through string and minimize frequency of opposite directions, calculating the changes if so
class Solution:
    def maxDistance(self, s: str, k: int) -> int:
        freq = defaultdict(int)
        ans = 0
        dirs_sum = 0 
        for c in s:
            freq[c] += 1
            dirs_sum += 1 # dirs_sum = sum(freq.values())
            num_of_opposite_dirs = min(freq["N"], freq["S"]) + min(freq["W"], freq["E"])
            man_dis = dirs_sum - (2 * num_of_opposite_dirs) 
            man_dis += (2 * min(k, num_of_opposite_dirs))
            ans = max(ans, man_dis)
        return ans
