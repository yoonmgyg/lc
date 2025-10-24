class Solution:
    def numberOfAlternaingGroups(self, colors: List[int], ans = 0) -> int:
        colors.extend(colors[0:2])

        for triple in zip(colors, colors[1:], colors[2:]):
            if (triple == (0, 1, 0)) or (triple == (1, 0, 1)):
                ans+= 1

        return ans
