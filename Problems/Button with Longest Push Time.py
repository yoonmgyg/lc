class Solution:
    def buttonWithLongestTime(self, events: List[List[int]]) -> int:
        
        max_diff = events[0][1]
        output = events[0][0]

        for i in range(1, len(events)):

            time_diff = events[i][1] - events[i - 1][1]
            
            if time_diff > max_diff:
                max_diff = time_diff
                output = events[i][0]

            elif max_diff == time_diff:
                output = min(output, events[i][0])


        return output
