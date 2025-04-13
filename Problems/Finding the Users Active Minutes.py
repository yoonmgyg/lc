class Solution:
    def findingUsersActiveMinutes(self, logs: List[List[int]], k: int) -> List[int]:
        res,  seen, d = [0] * k, set(), defaultdict(int)

        for user, time in logs:
            if (user, time) in seen:  continue
            d[user] += 1
            seen.add((user, time))
        
        for v in d.values():
            if v <= k:
                res[v-1] += 1
        
        return res
