# Converts date to binary by splitting through dashes and converting each value into binary and combining again
class Solution:
    def convertDateToBinary(self, date: str) -> str:
        year, month, day = date.split('-')

        year_bin = bin(int(year))[2:]    
        month_bin = bin(int(month))[2:] 
        day_bin = bin(int(day))[2:]     

        return f"{year_bin}-{month_bin}-{day_bin}"
