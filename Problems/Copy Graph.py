from typing import Dict, List

class IntGraphNode:
    def __init__(self, value = 0, neighbors = None):
        self.value = value
        self.neighbors = neighbors if neighbors is not None else []

class Solution:
    def copy_graph(self, node: IntGraphNode) -> Dict[int, List[int]]:
        adj_list = {}
        def dfs(node: IntGraphNode):
            if node.value in adj_list:
                return
            adj_list[node.value] = []
            for neighbor in node.neighbors:
                adj_list[node.value].append(neighbor.value)
                dfs(neighbor)

        if node:
            dfs(node)
            
        return adj_list
