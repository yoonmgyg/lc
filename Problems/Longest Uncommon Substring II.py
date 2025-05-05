class Solution:
    def findLUSlength(self, strs: List[str]) -> int:
        cnt = Counter(strs)
        
        strs.sort(key=len, reverse=True)
        
        def is_subseq(s: str, t: str) -> bool:
            i = 0
            for ch in t:
                if i < len(s) and s[i] == ch:
                    i += 1
                    if i == len(s):
                        return True
            return i == len(s)
        
        for i, s in enumerate(strs):
            if cnt[s] > 1:
                continue
            
            if all(not is_subseq(s, t) for j, t in enumerate(strs) if j != i):
                return len(s)
        
        return -1
