class Solution:
    def findEvenNumbers(self, digits: List[int]) -> List[int]:

        result = set()
        n = len(digits)
        
        even_digits = [d for d in digits if d % 2 == 0]
        for i in range(n):
            if digits[i] == 0: 
                continue
            for j in range(n):
                if j == i:
                    continue
                for k in range(n):
                    if k == i or k == j:
                        continue
                    # Ensure the last digit is even
                    if digits[k] % 2 == 0:
                        # Form the number and add to result
                        num = digits[i] * 100 + digits[j] * 10 + digits[k]
                        result.add(num)
        
        return sorted(result)
