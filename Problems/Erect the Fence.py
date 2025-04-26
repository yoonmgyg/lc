class Solution:
    def outerTrees(self, trees: List[List[int]]) -> List[List[int]]:
        trees.sort()
        points = defaultdict(list)
        for (x, y) in trees:
            points[x].append(y)
        
        def right_turn(x1, y1, x2, y2, x3, y3):
            return (y2 - y1) * (x3 - x1) > (y3 - y1) * (x2 - x1)

        def bottom():
            ans = []
            for x in sorted(points.keys()):
                y = points[x][0]
                ans.append((x, y))
                while True and len(ans) > 2:
                    x2, y2 = ans[-2]
                    x1, y1 = ans[-3]
                    if right_turn(x1, y1, x2, y2, x, y):
                        ans.pop(-2)
                    else:
                        break
            return ans

        def left_turn(x1, y1, x2, y2, x3, y3):
            return (y2 - y1) * (x3 - x1) < (y3 - y1) * (x2 - x1)
        
        def top():
            ans = []
            for x in sorted(points.keys()):
                y = points[x][-1]
                ans.append((x, y))
                while True and len(ans) > 2:
                    x2, y2 = ans[-2]
                    x1, y1 = ans[-3]
                    if left_turn(x1, y1, x2, y2, x, y):
                        ans.pop(-2)
                    else:
                        break
            return ans

        min_x = trees[0][0]
        max_x = trees[-1][0]
        start = [(min_x, y) for y in points[min_x]]
        end = [(max_x, y) for y in points[max_x]]

        return set(start + end + bottom() + top())
