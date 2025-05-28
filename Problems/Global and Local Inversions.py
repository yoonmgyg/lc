class Solution:
    def isIdealPermutation(self, A: List[int]) -> bool:
        numLoc = 0
        numGlo = 0

        for idx, num in enumerate(A):
            if num > idx:
                numGlo += (num-idx)
            elif num < idx:
                numGlo += (idx-num-1)
            
            if idx < len(A)-1 and num > A[idx+1]:
                numLoc += 1
        
        print(numLoc, numGlo)
        return numLoc == numGlo
