# Gets senior citizens by checking the 12 and 13th digit and checking if within senior age
class Solution:
    def countSeniors(self, details: List[str]) -> int:
        count = 0
        for i in details:
            age = int(i[11:13])  
            if age > 60:              
                count += 1            
        return count
