class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        number_of_negatives = 0
        for i in grid:
            for j in i:
                if j < 0:
                    number_of_negatives = number_of_negatives + 1

        return number_of_negatives
        
