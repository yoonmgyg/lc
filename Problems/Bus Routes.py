class Solution:
    def bus_routes(self, routes: List[List[int]], source: int, target: int):
        adj_list = {}
        for i, route in enumerate(routes):
            for stop in route:
                if stop not in adj_list:
                    adj_list[stop] = []
                adj_list[stop].append(i)

        visited = set()        
        queue = deque()

        for stop in adj_list[source]:
            queue.append((stop, 1))
            visited.add(stop)

        while queue:
            current, count = queue.popleft()
            if current == target:
                return count + 1

            for route in adj_list[current]:
                for stop in route:
                    if stop not in visited:
                        queue.append((stop, count + 1))
                        visited.add(stop)


        return -1
