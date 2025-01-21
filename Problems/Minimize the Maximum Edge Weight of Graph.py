
# Loop through edge cases and get unique weights, then use binary asearch to build reversed graph where weight <= mid, then finds the minimum possible value
class Solution:
    def minMaxWeight(self, n: int, edges: List[List[int]], threshold: int) -> int:
        if threshold == 0:
            if n == 1:
                return 0  
            else:
                return -1

        unique_weights = sorted({w for _, _, w in edges})
        reversed_graph = [[] for _ in range(n)]
        for u, v, w in edges:
            reversed_graph[v].append((u, w))

        def can_reach_all(mid):
            visited = [False]*n
            visited[0] = True
            queue = deque([0])

            while queue:
                curr = queue.popleft()
                for prev_node, w in reversed_graph[curr]:
                    if w <= mid and not visited[prev_node]:
                        visited[prev_node] = True
                        queue.append(prev_node)

            return all(visited)

        left, right = 0, len(unique_weights)-1
        answer = -1

        while left <= right:
            mid_idx = (left + right) // 2
            mid_val = unique_weights[mid_idx]

            if can_reach_all(mid_val):
                answer = mid_val
                right = mid_idx - 1
            else:
                left = mid_idx + 1

        return answer

