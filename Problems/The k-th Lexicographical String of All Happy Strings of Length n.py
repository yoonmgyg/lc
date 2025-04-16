class Solution:
    def getHappyString(self, n: int, k: int) -> str:
        from collections import deque
        q = deque(["a", "b", "c"])
        happy_strings = []
        
        while q:
            s = q.popleft()
            if len(s) == n:
                happy_strings.append(s)
                continue
            for ch in "abc":
                if s[-1] != ch:
                    q.append(s + ch)
        
        return "" if k > len(happy_strings) else happy_strings[k - 1]
