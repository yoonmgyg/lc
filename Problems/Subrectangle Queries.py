class SubrectangleQueries:
    def __init__(self, rectangle: List[List[int]]):
        self.r = copy.deepcopy(rectangle) # deep copy the input array - credit to @_xavier_
        self.histories = []

    def updateSubrectangle(self, row1: int, col1: int, row2: int, col2: int, newValue: int) -> None:
        self.histories.append([row1, col1, row2, col2, newValue])

    def getValue(self, row: int, col: int) -> int:
        for his in reversed(self.histories):
            if his[0] <= row <= his[2] and his[1] <= col <= his[3]:
                return his[4]
        return self.r[row][col]
