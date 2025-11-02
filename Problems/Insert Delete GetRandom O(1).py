class RandomizedSet:
    def __init__(self):
        self.values = []
        self.val_idx = {}
    def insert(self, val: int) -> bool:
        if val in self.val_idx:
            return False
        
        self.val_idx[val] = len(self.values)
        self.values.append(val)
        return True
    def remove(self, val: int) -> bool:
        if val not in self.val_idx:
            return False

        del_idx = self.val_idx[val]
        self.val_idx[self.values[-1]] = del_idx
        del self.val_idx[val]

        self.values[del_idx] = self.values[-1]
        self.values.pop()
        return True
    
    def getRandom(self) -> int:
        return self.values[random.randint(0, len(self.values) - 1)]
