class Solution:
    def power(self, x, y):
        result, power = 1.0, y
        if y < 0:
            power, x = -power, 1.0 / x
        while power:
            if power & 1:
                result *= x
            x, power = x * x, power >> 1
        return result
