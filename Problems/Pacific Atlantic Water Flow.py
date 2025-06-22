class Solution:
    def bfs(self, i: int, j: int, m: int, n: int, pna: List[bool], heights: List[List[int]]) -> None:
        q = deque([(i, j)])
        visited = [[False] * n for _ in range(m)]
        visited[i][j] = True

        while q:
            r, c = q.popleft()
            if r == m - 1 or c == n - 1:
                pna[1] = True
            if c == 0 or r == 0:
                pna[0] = True

            directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if 0 <= nr < m and 0 <= nc < n and heights[nr][nc] <= heights[r][c] and not visited[nr][nc]:
                    q.append((nr, nc))
                    visited[nr][nc] = True

    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        ans = []
        m, n = len(heights), len(heights[0])

        for i in range(m):
            for j in range(n):
                pna = [False, False]
                self.bfs(i, j, m, n, pna, heights)
                if pna[0] and pna[1]:
                    ans.append([i, j])

        return ans
