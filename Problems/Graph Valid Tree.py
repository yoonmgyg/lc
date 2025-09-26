class Solution:
    def graph_valid_tree(self, n: int, edges: List[List[int]]):
        # Your code goes here
        if n == 0:
            return False
        
        adj_list = {i : [] for i in range (n)}
        for u, v in edges:
            adj_list[u].append(v)
            adj_list[v].append(u)

        visited = set()
        node_count = 0
        def dfs(node, parent):
            nonlocal node_count
            if node in visited:
                return False
            visited.add(node)
            node_count += 1
            for neighbor in adj_list[node]:
                if neighbor == parent:
                    continue
                if not dfs(neighbor, node):
                    return False
            return True

        return dfs(0, -1) and len(visited) == n
