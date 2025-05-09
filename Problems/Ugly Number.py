# Check for ugly number by continually dividing by 2, 3, 5
class Solution:
    def isUgly(self, n: int) -> bool:
        if n == 0:
            return 0
        for i in 2,3,5:
            while n % i==0:
                n //= i
        return n == 1
