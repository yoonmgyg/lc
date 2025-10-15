class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adj_list = defaultdict(list)
        indegrees = [0] * numCourses
        for dest, src in prerequisites:
            adj_list[src].append(dest)
            indegrees[dest] += 1

        queue = deque([i for i in range(numCourses) if indegrees[i] == 0])
        res = []
        while queue:
            curr = queue.popleft()
            res.append(curr)
            for dest in adj_list[curr]:
                indegrees[dest] -= 1
                if indegrees[dest] == 0:
                    queue.append(dest)
        
        return res if len(res) == numCourses else []
