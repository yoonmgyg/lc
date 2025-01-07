# Loops through integer and gets last digit, multiplies product and gets the sum and subtracts at the end
def subtractProductAndSum(self, n: int) -> int:
        prod = 1        
        sums = 0
        while n != 0:       
            last = n % 10   
            prod *= last    
            sums += last    
            n = n // 10        
        return prod - sums  
