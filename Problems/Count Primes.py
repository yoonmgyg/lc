class Solution:
    def countPrimes(self, n: int) -> int:
            if n < 3: return 0    
            lst = [1] * n          
            lst[0] = lst[1] = 0    
            m = 2
            while m * m < n:      
                if lst[m] == 1:    
                m += 1 if m == 2 else 2
            return sum(lst)
