class Solution:
    def slowestKey(self, releaseTimes: List[int], keysPressed: str) -> str:
        slowest = 0
        key = 0
        prev_key = 0
        for i in range(len(releaseTimes)):
            diff =  releaseTimes[i] - prev_key
            if diff > slowest:
                slowest = diff
                key = i
            elif diff == slowest:
                if keysPressed[i] > keysPressed[key]:
                    key = i
            prev_key = releaseTimes[i]
        return keysPressed[key]
