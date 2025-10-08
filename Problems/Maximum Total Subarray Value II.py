class Solution:
    def maxTotalValue(self, A: List[int], K: int) -> int:
        N = len(A)
        smin = SparseTableOp(A, min)
        smax = SparseTableOp(A, max)
        
        pq = []
        for i in range(N):
            v = smax.query(i, N-1) - smin.query(i, N-1)
            pq.append([-v, i, N-1])
        heapify(pq)

        ans = 0
        for _ in range(K):
            nv, i, j = heappop(pq)
            ans -= nv
            if j - 1 >= i:
                v2 = smax.query(i, j-1) - smin.query(i, j-1)
                heappush(pq, [-v2, i, j-1])

        return ans

class SparseTableOp:
    def __init__(self, arr, op):
        self.n = len(arr)
        self.k = int(math.log2(self.n)) + 1
        self.table = [[0] * self.k for _ in range(self.n)]
        self.op = op

        for i in range(self.n):
            self.table[i][0] = arr[i]

        for j in range(1, self.k):
            for i in range(self.n - (1 << j) + 1):
                self.table[i][j] = op(
                    self.table[i][j - 1], self.table[i + (1 << (j - 1))][j - 1]
                )

    def query(self, left, right):
        length = right - left + 1
        k = int(math.log2(length))
        return self.op(self.table[left][k], self.table[right - (1 << k) + 1][k])
