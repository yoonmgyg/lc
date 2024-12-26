% Checks if double reversed number is same by determining if it is divisible by 10
class Solution:
    def isSameAfterReversals(self, num: int) -> bool:
        if num % 10 == 0 and num != 0:
            return False
        return True
