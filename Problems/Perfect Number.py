class Solution:
    def checkPerfectNumber(self, num: int) -> bool:
        if num <= 1:
            return False
        total = 0
        for i in range(1, num):
            if num % i == 0:
                total += i
        return total == num
