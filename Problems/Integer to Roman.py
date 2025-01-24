# Loop through roman integers backwards and add the symbol times each value
class Solution:
    def intToRoman(self, num: int) -> str:
        res = ""
        roman = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }
        res = []

        for symbol, value in sorted(roman.items(), key=lambda x: x[1], reverse=True):
            if num == 0:
                break
            count = num // value
            res.append(symbol * count)
            num -= count * value

        return ''.join(res)
