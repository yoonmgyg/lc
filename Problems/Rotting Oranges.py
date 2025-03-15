from collections import deque

class Solution:
    def orangesRotting(self, grid):
        m, n = len(grid), len(grid[0])
        queue = deque()
        fresh = 0

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 2:
                    queue.append((i, j))
                elif grid[i][j] == 1:
                    fresh += 1

        if fresh == 0:
            return 0

        minutes = 0
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        while queue:
            size = len(queue)
            spread = False

            for _ in range(size):
                x, y = queue.popleft()

                for dx, dy in directions:
                    nx, ny = x + dx, y + dy

                    if 0 <= nx < m and 0 <= ny < n and grid[nx][ny] == 1:
                        grid[nx][ny] = 2  
                        queue.append((nx, ny))
                        fresh -= 1
                        spread = True

            if spread:
                minutes += 1

        return minutes if fresh == 0 else -1
