class Solution:
    def kthDistinct(self, arr: list[str], k: int) -> str:
        count = 0
        map = {}

        for item in arr:
            if item in map:
                map[item] = False  # Mark as not distinct
            else:
                map[item] = True  # Mark as distinct

        for item in arr:
            if map[item]:  # Check if it's distinct
                count += 1
                if count == k:
                    return item

        return ""
