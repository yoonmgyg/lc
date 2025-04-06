class Solution:
    def complexNumberMultiply(self, num1: str, num2: str) -> str:
        a1, b1 = num1.split('+')
        a1 = int(a1)
        b1 = int(b1[:-1])
        a2, b2 = num2.split('+')
        a2 = int(a2)
        b2 = int(b2[:-1])
        return str(a1 * a2 + b1 * b2 * (-1)) + '+' + str(a1 * b2 + a2 * b1) + 'i'
