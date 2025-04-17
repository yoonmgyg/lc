class Solution:
    def checkString(self, s: str) -> bool:
        a_right_index = s.rfind('a')
        b_left_index = s.find('b')

        if (a_right_index >= 0 and b_left_index >= 0):
            return a_right_index < b_left_index
        else:
            return True
