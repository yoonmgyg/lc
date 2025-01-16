# Flips column by getting inverse of eah row and checking if row is equal
class Solution:
    def maxEqualRowsAfterFlips(self, mat: list[list[int]]) -> int:
        n = len(mat)
        m = len(mat[0])
        ans = 0

        for bin_row in mat:
            inv_bin = [1 - val for val in bin_row]
            tmp = 0
            for cur_row in mat:
                if cur_row == bin_row or cur_row == inv_bin:
                    tmp += 1

            ans = max(tmp, ans)

        return ans
