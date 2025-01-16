# Keep track of bar and asterisks and add if no bar is present
class Solution: 
    def countAsterisks(self, s: str) -> int:
        bar = False
        count = 0
        for x in s:
            if x == '|':
                bar = not bar
                    
            if x == '*' and bar == False:
                count+=1

        return ans
