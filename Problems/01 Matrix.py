class Solution:
    def updateMatrix(self, mat: List[List[int]]):
        m = len(mat)
        n = len(mat[0])

        queue = deque()
        dist = [[float('inf')] * n for _ in range(m)]
        for i in range(m):
            for j in range(n):
                if mat[i][j] == 0:
                    queue.append((i, j))
                    dist[i][j] = 0
        
        if not queue:
            return [[-1 for i in range(n)] for i in range(m)]
        
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        while queue:
            r, c = queue.popleft()
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if 0 <= nr < m and 0 <= nc < n:
                    if dist[nr][nc] > dist[r][c]:
                        queue.append((nr, nc))
                        dist[nr][nc] = dist[r][c] + 1

        return dist   
                
