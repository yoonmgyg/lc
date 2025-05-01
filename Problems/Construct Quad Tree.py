class Solution:
    def construct(self, grid: List[List[int]]) -> 'Node':
        def construct_range(top, left, l):
            if l == 1:
                return Node(grid[top][left], True)
            topLeft = construct_range(top, left, l // 2)
            topRight = construct_range(top, left + l // 2, l // 2)
            botLeft = construct_range(top + l // 2, left, l // 2)
            botRight = construct_range(top + l // 2, left + l // 2, l // 2)

            children = [topLeft, topRight, botLeft, botRight]
            if all(child.isLeaf and child.val == topLeft.val for child in children):
                return Node(topLeft.val, True)
            
            return Node(0, False, topLeft, topRight, botLeft, botRight)
        
        return construct_range(0, 0, len(grid))
