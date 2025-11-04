class Solution:
    def myAtoi(self, s: str) -> int:
        if not s:
            return 0
        n = len(s)
        i = 0
        while i < n and s[i] == ' ':
            i += 1
        
        if i == n:
            return 0
        
        sign = 1
        if s[i] == '+' or s[i] == '-':
            sign = -1 if s[i] == '-' else 1
            i += 1
        
        number = 0
        while i < n and s[i].isdigit():
            number *= 10
            number += int(s[i])
            i += 1

            if sign * number >= 2**31 - 1:
                return 2**31 - 1
            if sign * number <= -2**31:
                return -2**31
        return number * sign
