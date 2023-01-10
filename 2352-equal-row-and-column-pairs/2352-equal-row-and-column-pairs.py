class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        column =list(zip(*grid))
        count = 0
        c = 0
        print("co", column)
        size = len(column)
        dict_ = {}
        
        for i in grid:    
            i = tuple(i)
            if i in dict_:
                dict_[i] +=1
            else:
                dict_[i] = 0
            for j in range(size):
                if column[j] == i:
                    count +=1

        return count
            