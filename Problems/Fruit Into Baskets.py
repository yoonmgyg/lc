# Use sliding windows to get range of fruits in basket
class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        basket = {}
        max_fruit = 0
        start = 0

        for end in range(len(fruits)):
            basket[fruits[end]] = basket.get(fruits[end], 0) + 1
            while len(basket) > 2:
                basket[fruits[start]] -= 1
                if basket[fruits[start]] == 0:
                    del basket[fruits[start]]
                start += 1
            
            max_fruit = max(max_fruit, end - start + 1)
        
        return max_fruit
