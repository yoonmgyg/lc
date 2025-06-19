class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        prod, summ = 1, 0
        for car in str(n):
            prod *= int(car)
            summ += int(car)
        return prod - summ
