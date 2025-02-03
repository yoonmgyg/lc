# Get frequencies and append based on mod, then get the max and min of both
class Solution:
    def maxDifference(self, s):
        from collections import Counter
    
        frequency = Counter(s)
        even_freq = []
        odd_freq = []
        for char, freq in frequency.items():
            if freq % 2 == 0:
                even_freq.append(freq)
            else:
                odd_freq.append(freq)
    
        if not even_freq or not odd_freq:
            return 0
    
        max_odd = max(odd_freq)
        min_even = min(even_freq)
    
        difference = max_odd - min_even
    
        return difference
