class Solution:
    def numRookCaptures(self, board: List[List[str]]) -> int:
        def check_direction(R,C,direction):
            if direction=="right":
                for col in range(C+1,8):
                    if board[R][col].islower(): return 1
                    if board[R][col].isupper(): return 0
            if direction=="left":
                for col in range(C-1,-1,-1): 
                    if board[R][col].islower(): return 1
                    if board[R][col].isupper(): return 0
            if direction=="down":
                for row in range(R+1,8): 
                    if board[row][C].islower(): return 1
                    if board[row][C].isupper(): return 0
            if direction=="up": 
                for row in range(R-1,-1,-1):
                    if board[row][C].islower(): return 1
                    if board[row][C].isupper(): return 0
            return 0 
                    
        for row in range(8):
            for col in range(8):
                if board[row][col]=="R":
                    return sum([check_direction(row,col,"right"),
                                check_direction(row,col,"left"),
                                check_direction(row,col,"up"),
                                check_direction(row,col,"down")])
