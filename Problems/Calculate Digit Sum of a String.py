class Solution:
    def digitSum(self, s, k):
        len_s = len(s)
        
        while (len_s > k):
            new_s = ''
            start_index = 0
            end_pos = start_index + k
            
            while (start_index < len_s):
                substr = s[start_index:end_pos]
                sum_digits = sum([int(d) for d in list(substr)])
                new_s += str(sum_digits)
                start_index += k
                end_pos += k
            s = new_s
            len_s = len(s)
        
        return s
