class Solution:
    def generateParenthesis(self, n: int):
        res = []
        def backtrack(s, open, closed):
            if len(s) == n * 2:
                res.append(s[:])
                return

            if open < n:
                backtrack(s + "(", open + 1, closed)
            
            if closed < open:
                backtrack(s + ")", open, closed + 1)

        backtrack("", 0, 0)
        return res
