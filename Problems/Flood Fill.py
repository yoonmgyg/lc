class Solution:
    def flood_fill(self, image: List[List[int]], sr: int, sc: int, color: int):
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        if color == image[sr][sc]:
            return image

        def dfs(sr, sc, color, orig):
            if (sr < 0 or sr >= len(image) or sc < 0 or sc >= len(image[0])):
                return
            
            if image[sr][sc] != orig:
                return
            
            image[sr][sc] = color

            for dr, dc in directions:
                dfs(sr + dr, sc + dc, color, orig)

        dfs(sr, sc, color, image[sr][sc])
        return image
