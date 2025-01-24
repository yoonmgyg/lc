# Use dict to set roman values and loop through values, subtracting if first element if lesser
class Solution:
    def romanToInt(self, s: str) -> int:
        roman = {
            "I" = 1
            "V" = 5
            "X" = 10
            "L" = 50
            "C" = 100
            "D" = 500
            "M" = 1000
        }

        for a, b in zip(s, s[1:]):
            if (roman[a] < roman[n]):
                res -= roman[a]
            else:
                res += roman[a]
            
        return res + roman[s[-1]]
