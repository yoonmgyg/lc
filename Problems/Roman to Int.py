class Solution:
    def romanToInt(self, s: str) -> int:
        res = 0
        roman_val = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }

        for i in range(len(s)-1):
            if roman_val[s[i]] < roman_val[s[i+1]]:
                res -= roman_val[s[i]]
            else:
                res += roman_val[s[i]]

        res += roman_val[s[-1]]
        return res 
