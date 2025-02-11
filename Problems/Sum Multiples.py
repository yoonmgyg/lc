# Loop through numbers and modulo by 3, 5, 7
class Solution:
    def sumOfMultiples(self, n: int) -> int:
        res = 0
        for i in range(3, n + 1):
            if i % 3 == 0 or i % 5 == 0 or i % 7 == 0:
                res += i
        return res
