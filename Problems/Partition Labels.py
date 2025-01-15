# Gets last occurrence of character and loops through string, updating maximum position with last occuring char
class Solution:
    def partitionLabels(s: str) -> list[int]:
        last_occurrence = {}
        for i, char in enumerate(s):
            last_occurrence[char] = i
    
        result = []
        start = 0
        max_pos = 0
    
        for i, char in enumerate(s):
            max_pos = max(max_pos, last_occurrence[char])
            if i == max_pos:
                result.append(i - start + 1)
                start = i + 1
    
        return result
