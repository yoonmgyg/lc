# Gets lucky number by finding minimum element and checking column if it is maximum
class Solution:
    def luckyNumbers(self, matrix):
        ans = []
        n = len(matrix)
        m = len(matrix[0])
        
        for i in range(n):
            row_min = min(matrix[i])
            row_min_index = matrix[i].index(row_min)
            
            is_lucky = True
            for k in range(n):
                if matrix[k][row_min_index] > row_min:
                    is_lucky = False
                    break
            
            if is_lucky:
                ans.append(row_min)
        
        return ans
