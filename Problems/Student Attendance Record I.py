# Loop through string and check chars for attendance
class Solution:
    def checkRecord(self, s: str) -> bool:
        A = 0
        L = 0
        for i in s:
            if i == "A":
                A += 1
            elif i == "L":
                L += 1
        if A >= 2:
            return False
        elif "LLL" in s:
            return False
        else:
            return True
