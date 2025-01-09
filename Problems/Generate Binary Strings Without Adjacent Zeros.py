# Generates binary string by using backtracking to append possible sequences and making sure each contains 1 between zeroes
class Solution:
    def validStrings(self, n):
        result = []
        self.generateStrings(result, [], n, -1)
        return result

    def generateStrings(self, result, sb, n, lastChar):
        if len(sb) == n:
            result.append(''.join(sb))
            return

        sb.append('1')
        self.generateStrings(result, sb, n, 1)
        sb.pop()

        if lastChar != 0:
            sb.append('0')
            self.generateStrings(result, sb, n, 0)
            sb.pop()
