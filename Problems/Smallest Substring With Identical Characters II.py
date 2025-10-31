class Solution:
    def minLength(self, s: str, numOps: int) -> int:
        A = list(map(int, s))
        L = [len(list(it)) for a, it in groupby(A)]
        def check(A, k):
            if k == 1:
                res = sum(a == i % 2 for i,a in enumerate(A))
                return min(res, len(A) - res)
            return sum(l // (k + 1) for l in L)
        l, r = 1, 100000
        while l < r:
            m = (l + r) // 2
            need = check(A, m)
            if need <= numOps:
                r = m
            else:
                l = m + 1
        return l
