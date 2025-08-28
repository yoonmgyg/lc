class Solution:
    def decodeString(self, s: str):
        stack = []
        curr_str = ""
        curr_int = 0
        for ch in s:
            if ch == '[': # store integer and string into stach before bracket
                stack.append(curr_int)
                stack.append(curr_str)
                curr_str = ""
                curr_int = 0
            elif ch == ']': # add previous integer and string
                last_str = stack.pop()
                last_int = stack.pop()
                curr_str = last_str + last_int * curr_str
            elif ch.isdigit():
                curr_int *= 10
                curr_int += int(ch)
            else:
                curr_str += ch
        return curr_str
