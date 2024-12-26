# Gets the number of water bottles through recursively dividing drunk water bottles to get new bottles
class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        result = numBottles
        drunk, empty = divmod(numBottles, numExchange)
        while drunk:
            result += drunk
            drunk, empty = divmod(empty + drunk, numExchange)
        return result
