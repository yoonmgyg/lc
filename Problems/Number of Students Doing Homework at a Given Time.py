# Loop through students and check if within start and endtime at the same index
class Solution:
    def busyStudent(self, startTime: List[int], endTime: List[int], queryTime: int) -> int:
        doingHomework = 0
        
        for idx in range(len(startTime)):
            if startTime[idx] <= queryTime <= endTime[idx]:
                doingHomework += 1
        
        return doingHomework
