class Solution:
    def uniqueOccurrences(self, arr: list[int]) -> bool:
        freq_map = {}
        freq_set = set()
        
        for num in arr:
            freq_map[num] = freq_map.get(num, 0) + 1
        
        for count in freq_map.values():
            freq_set.add(count)
        
        return len(freq_map) == len(freq_set)
