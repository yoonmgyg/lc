class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        if not mat or not mat[0]:
            return []
        m, n = len(mat), len(mat[0])
        result = []

        for k in range(m + n - 1):
            diagonal = []
            row_start = max(0, k - (n - 1))
            row_end   = min(m - 1, k)
            for i in range(row_start, row_end + 1):
                j = k - i
                diagonal.append(mat[i][j])

            if k % 2 == 0:
                diagonal.reverse()

            result.extend(diagonal)

        return result
