class RandomizedSet:
    def __init__(self):
        self.set_ = []
        self.index = {}
        
    def insert(self, val: int) -> bool:
        if val in self.index:
            return False
        
        self.set_.append(val)
        self.index[val] = len(self.set_) - 1
        return True
        
    def remove(self, val: int) -> bool:
        if val not in self.index:
            return False
        idx = self.index[val]
        self.index[self.set_[-1]] = idx

        self.set_[idx], self.set_[-1] = self.set_[-1], self.set_[idx]
        self.set_.pop()
        del self.index[val]
        return True        

    def getRandom(self) -> int:
        return random.choice(self.set_)       


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()