# Gets the fibonacci number through a DP list to add previous numbers
class Solution:
    def fib(self, n: int) -> int:
        if n <= 1:
            return n

        # initialize fibonacci list
        f = [0] * (n + 1)  
        f[0] = 1
        f[1] = 1

        for i in range(2, n + 1):
            # use previous 2 numbers to calculate next number
            f[i] = f[i - 1] + f[i - 2]

        return f[n]
