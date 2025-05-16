class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        if not matrix:
            return 0
        
        rows, cols = len(matrix), len(matrix[0])
        heights = [0] * (cols + 1) 
        max_area = 0
        
        for row in matrix:
            for i in range(cols):
                heights[i] = heights[i] + 1 if row[i] == '1' else 0
            
            n = len(heights)  

            for i in range(n):
                for j in range(i, n):
                    min_height = min(heights[k] for k in range(i, j + 1))
                    area = min_height * (j - i + 1)
                    if area > max_area:
                        max_area = area

        return max_area
        
