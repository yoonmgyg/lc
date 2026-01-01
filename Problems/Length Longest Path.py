class Solution:
    def lengthLongestPath(self, s: str) -> int:
        paths, stack, ans = s.split('\n'), [], 0
        for path in paths:
            p = path.split('\t')
            depth, name = len(p) - 1, p[-1]
            l = len(name)
            while stack and stack[-1][1] >= depth: stack.pop()
            if not stack: stack.append((l, depth))
            else: stack.append((l+stack[-1][0], depth))
            if '.' in name: ans = max(ans, stack[-1][0] + stack[-1][1])   
        return ans
