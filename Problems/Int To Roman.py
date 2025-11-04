class Solution:
    def intToRoman(self, num: int) -> str:
        res = ""
        roman_vals = {
            'M': 1000,
            'CM': 900,
            'D': 500,
            'CD': 400,
            'C': 100,
            'XC': 90,
            'L': 50,
            'XL': 40,
            'X': 10,
            'IX': 9,
            'V': 5,
            'IV': 4,
            'I': 1
        }


        for key, val in roman_vals.items():
            if num == 0:
                return res
            
            res += key * (num // val)
            num -= num // val * val
        
        return res
