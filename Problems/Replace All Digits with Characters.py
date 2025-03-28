class Solution:
    def replaceDigits(self, s: str) -> str:

        lst = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
        sol = []

        for i in range(1,len(s)):
            if s[i-1].isalpha():
                sol.append(s[i-1])

            if s[i].isdigit():
                ind = lst.index(s[i-1])
                new_ind = ind + int(s[i])
                sol.append(lst[new_ind])
        if s and s[-1].isalpha():
            sol.append(s[-1])
            

        return ''.join(sol)
