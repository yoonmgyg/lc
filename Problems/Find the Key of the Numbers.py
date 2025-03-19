class Solution(object):
    def generateKey(self, num1, num2, num3):
        vec = [str(num1), str(num2), str(num3)]
        
        for i in range(3):
            vec[i] = vec[i].zfill(4)  
        
        ans = "" 
        
        for i in range(4):
            ch = min(vec[0][i], vec[1][i], vec[2][i])
            ans += ch

        return int(ans)
