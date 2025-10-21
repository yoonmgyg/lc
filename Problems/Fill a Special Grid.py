class Solution:
    def specialGrid(self, N: int) -> List[List[int]]:
        def generateGrid(n, offset):
            if n == 0:
                return [[offset]]

            size = 2 ** (n - 1)
            quad = 4 ** (n - 1)

            t_right = generateGrid(n-1, offset)
            b_right = generateGrid(n-1, offset + quad)
            b_left = generateGrid(n-1, offset + 2 * quad)
            t_left = generateGrid(n-1, offset + 3 * quad)

            top = [topl + topr for topl, topr in zip(t_left, t_right)]
            bottom = [botl + botr for botl, botr in zip(b_left, b_right)]
            return top + bottom
    
        return generateGrid(N, 0)
