class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        def dfs(root, output):
            if not root:
                return None
            output.append(root.val)
            for child in root.children:
                dfs(child, output)
            return output
        
        return dfs(root, [])
