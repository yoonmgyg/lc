class Solution:
    def finalValueAfterOperations(self, operations: List[str]) -> int:
        answer = 0
        for operation in operations:
            if operation in {'X--', '--X'}:
                answer -= 1
            elif operation in {'X++', '++X'}:
                answer += 1
        return answer
