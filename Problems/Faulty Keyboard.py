class Solution:
    def finalString(self, s):
        len_s = len(s)

        ret_val = ''

        i = 0
        while (i < len_s):
            if (s[i] == 'i'):
                ret_val = ret_val[::-1]
            else:
                ret_val += s[i]

            i += 1

        return ret_val
