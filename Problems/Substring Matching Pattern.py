class Solution:
    def hasMatch(self, s: str, p: str) -> bool:
        a, b = p.split('*')
        idxa = s.find(a)
        
        if idxa == -1:
            return False
        else:
            idxa += len(a)

        return True if b == '' or b in s[idxa:] else False          
