class Solution:
    def longestBalanced(self, s: str) -> int:
        n = len(s)
        ans = 0

        def is_balanced(freq, tar):
            for f in freq:
                if f != 0 and f != tar:
                    return False
            return True

        for i in range(n):
            freq = [0] * 26
            for j in range(i, n):
                freq[ord(s[j]) - ord('a')] += 1
                if is_balanced(freq, freq[ord(s[j]) - ord('a')]):
                    ans = max(ans, j - i + 1)
        return ans
