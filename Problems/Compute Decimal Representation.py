class Solution:
    def decimalRepresentation(self, n: int) -> List[int]:
        components = []
        digit = 0
        while n > 0:
            current = n % 10
            if (current != 0):
                components.insert(0, (n % 10) * 10 ** digit)
            n //= 10
            digit += 1

        return components
