class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        ans = []   
            
        def backtrack(index, subset):
            sum_ = sum(subset)
            if sum_ == target:
                ans.append(subset)
                return
            if sum_ > target:
                return
            
            for i in range(index, len(candidates)):
                backtrack(i, subset + [candidates[i]])

        backtrack(0, [])
        return ans

        # ans = []
        
        # def backtrack(index, subset):
        #     if sum(subset) == target:
        #         subset = sorted(subset)
        #         if subset not in ans:
        #             ans.append(subset)
        #         return
        #     elif sum(subset) > target:
        #         return
            
        #     for i in range(len(candidates)):
        #         backtrack(i, subset + [candidates[i]])

        # backtrack(0, [])
        # return ans