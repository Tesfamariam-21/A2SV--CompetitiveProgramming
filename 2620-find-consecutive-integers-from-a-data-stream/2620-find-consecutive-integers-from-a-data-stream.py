class DataStream:

    def __init__(self, value: int, k: int):
        self.count = 0
        self.value = value
        self.k = k        

    def consec(self, num: int) -> bool:
        if num == self.value:
            self.count +=1
        else:
            self.count = 0

        return self.count > self.k - 1

    #def __init__(self, value: int, k: int):
    #     self.arr = []
    #     self.value = value
    #     self.k = k        

    # def consec(self, num: int) -> bool:
    #     self.arr.append(num)
    #     if len(self.arr) < self.k:
    #         return False

    #     for i in range(self.k):
    #         if self.arr[len(self.arr) - i - 1] != self.value:
    #             return False

    #     return True
        


# Your DataStream object will be instantiated and called as such:
# obj = DataStream(value, k)
# param_1 = obj.consec(num)