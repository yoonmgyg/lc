class Solution:
    def maxSumDistinctTriplet(self, x: List[int], y: List[int]) -> int:
        n = len(x)
    
        best_y_for_x = dict()
        for idx in range(n):
            if x[idx] not in best_y_for_x or y[idx] > best_y_for_x[x[idx]][0]:
                best_y_for_x[x[idx]] = (y[idx], idx)
    
        if len(best_y_for_x) < 3:
            return -1
    
        candidates = sorted(
            [(y_val, x_val, idx) for x_val, (y_val, idx) in best_y_for_x.items()],
            reverse=True
        )
    
        result = candidates[0][0] + candidates[1][0] + candidates[2][0]
        return result©leetcode
