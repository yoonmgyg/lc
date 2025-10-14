def combinationSum(candidates, target):
    def backtrack(start, combo, current_target):
        if current_target == 0:
            result.append(list(combo))
            return
        for i in range(start, len(candidates)):
            curr = candidates[i]
            if candidates[i] > current_target:
                return
            combo.append(curr)
            backtrack(i, combo, current_target - curr)
            combo.pop()
        return
    
    candidates.sort()
    result = []
    backtrack(0, [], target)
    return result
