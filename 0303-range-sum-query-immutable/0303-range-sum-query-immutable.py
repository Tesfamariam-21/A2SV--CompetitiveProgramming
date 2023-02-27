class NumArray:

    def __init__(self, nums: List[int]):
        self.numArray = nums
        

    def sumRange(self, left: int, right: int) -> int:
        sum_ = 0
        for i in range(left, right+1):
            sum_ += self.numArray[i]
            
            
        return sum_
        
        


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)