class Solution:
    def assignElements(self, groups: List[int], elements: List[int]) -> List[int]:           
        candidate = {}
        for j, val in enumerate(elements):
            if val not in candidate:
                candidate[val] = j
    
        divisor_cache = {}
        assigned = []
        
        for g in groups:
            if g not in divisor_cache:
                divs = set()
                for i in range(1, int(math.isqrt(g)) + 1):
                    if g % i == 0:
                        divs.add(i)
                        divs.add(g // i)
                divisor_cache[g] = list(divs)
            
            best_index = float('inf')
            for d in divisor_cache[g]:
                if d in candidate:
                    best_index = min(best_index, candidate[d])
            
            assigned.append(best_index if best_index != float('inf') else -1)
        
        return assigned
