# Find the complement by flipping each bit
class Solution:
    def findComplement(self, num: int) -> int:
        binary = bin(num)[2:]
        flip = ""
        for bit in binary:
            if bit == "0":
                flip += "1"
            else:
                flip += "0"
        return int(flip, 2)
