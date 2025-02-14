# Calculate area of rectangles subtracting the intersection
class Solution:
    def computeArea(self, A: int, B: int, C: int, D: int, E: int, F: int, G: int, H: int) -> int:
        
        left_boundary = max(A, E)
        right_boundary = min(C, G)
        
        top_boundary = min(D, H)
        bottom_bondary = max(B, F)
        
        
        area_1 = (C - A)*(D - B)
        area_2 = (G - E)*(H - F)
        
        if (left_boundary < right_boundary) and (bottom_bondary < top_boundary):
            intersection = ( right_boundary - left_boundary ) * ( top_boundary - bottom_bondary )
			
        else:
            intersection = 0
        
        return area_1 + area_2 - intersection
