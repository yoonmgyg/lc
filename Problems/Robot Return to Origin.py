# Keeps track of robot coords and see if results are 0
class Solution:
    def judgeCircle(self, moves: str) -> bool:
        lr, ud = 0 , 0

        for move in moves:
            if move == 'U':
                ud += 1
            elif move == 'D':
                ud -= 1
            elif move == 'L':
                lr += 1
            elif move == 'R':
                lr -= 1

        if lr == 0 and ud == 0:
            return True
