# Check for self dividing number by looping through rightmost digit and checking for divisibility
class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        self_div = []
        while left <= right:
            n = left
            while n != 0 and n % 10 != 0:
                if left % (n % 10) == 0:
                    n //= 10
                else:
                    break
            if n == 0:
                list_self_div.append(left)
            left += 1
        return list_self_div
