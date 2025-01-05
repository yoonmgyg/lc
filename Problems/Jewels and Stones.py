# Use set to get jewels and loop through stones to see if in set
class Solution:
    def numJewelsInStones(self, J: str, S: str) -> int:
        counter = 0
        jewels = set(J) 
        for stone in S:
            if stone in jewels:
                counter += 1
        return counter
