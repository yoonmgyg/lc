# Use set to keep track of strings and check adjacent to determine if special
class Solution:
    def hasSpecialSubstring(self, s: str, k: int) -> bool:
        for i in range(len(s)):
            chars = set() 
            for j in range(i, len(s)):  
                chars.add(s[j]) 
                if len(chars) > 1: 
                    break  
                if (j - i) == k - 1:  
                    if (j + 1 < len(s) and s[j + 1] in chars) or (i > 0 and s[i - 1] in chars):
                        break  
                    return True  
        return False  
