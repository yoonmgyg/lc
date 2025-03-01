class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:       
        n = len(triangle)
        for i in range(1, n):
            for j in range(i, -1, -1): 
                up = triangle[i-1][j] if j < i else float('inf')
                upLeft = triangle[i-1][j-1] if j-1 >= 0 else float('inf')
                triangle[i][j] += min(up, upLeft)

        return min(triangle[n-1])  
