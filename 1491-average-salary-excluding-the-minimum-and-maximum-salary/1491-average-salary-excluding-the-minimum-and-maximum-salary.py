class Solution:
    def average(self, salary: List[int]) -> float:
        salary.sort()
        sum_ = 0
        size = len(salary)-2
        
        for i in range(1, (len(salary) - 1)):
            sum_ += salary[i]
            
        return sum_/size
            
        