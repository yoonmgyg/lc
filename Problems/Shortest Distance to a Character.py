class Solution(object):
    def shortestToChar(self, s, c):
        ans = [0] * len(s)
        l = 0
        prevr = -1
        for r in range(len(s)):
            if s[r] == c:
                while l <= r:
                    if prevr != -1:
                        ans[l] = min(r-l, l-prevr)
                    else:
                        ans[l] = r - l
                    l += 1
                prevr = r
        while l < len(s):
            ans[l] = l - prevr
            l += 1
        return ans
