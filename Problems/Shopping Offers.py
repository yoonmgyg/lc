# Use dfs to calculate cost and loop through specials to get min cost
class Solution:
    def shoppingOffers(self, price: List[int], specials: List[List[int]], needs: List[int]) -> int:

        @lru_cache(None)
        def dfs(needs):
            cost = sum(map(mul, needs, price))        
            for special in specials:
                specPrice = special.pop()
                tmp = tuple(map(sub, needs, special))   
                if min(tmp) < 0: 
                    continue             
                cost = min(cost, dfs(tmp)) + specPrice  

            return cost                                 

        return dfs(tuple(needs))
