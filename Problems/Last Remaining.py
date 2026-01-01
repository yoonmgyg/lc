class Solution(object):
    def lastRemaining(self, n):
        def helper(x, step, count, direction):
            if count < 2:
                return x
            increment = step if direction or count % 2 else 0
            return helper(x + increment, step * 2, count // 2, not direction)

        return helper(1, 1, n, True)
