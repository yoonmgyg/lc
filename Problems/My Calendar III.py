from sortedcontainers import SortedDict
# Uses the sweeping line through a sorted dictionary to get overlapping elements in calendar
# Time Complexity: O(N ^ 2)
# Space Complexity: O(N)
class MyCalendarThree:
    def __init__(self):
        self.lines = SortedDict()
      
    def book(self, start: int, end: int) -> int:
        self.lines[start] = self.lines.get(start, 0) + 1
        self.lines[end] = self.lines.get(end, 0) - 1
        return max(accumulate(self.lines.values()))

