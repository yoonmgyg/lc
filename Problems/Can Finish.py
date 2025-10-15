class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]):
        adj_list = defaultdict(list)
        indegrees = [0] * numCourses
        for u, v in prerequisites:
            adj_list[v].append(u)
            indegrees[u] += 1
        
        queue = deque([u for u in range(numCourses) if indegrees[u] == 0])
        order = []
        while queue:
            curr = queue.popleft()
            order.append(curr)
            for neighbor in adj_list[curr]:
                indegrees[neighbor] -= 1
                if indegrees[neighbor] == 0:
                    queue.append(neighbor)
        
        return numCourses == len(order)
