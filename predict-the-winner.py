class Solution:
    def PredictTheWinner(self, nums: List[int]) -> bool:
        
        def predict(nums, start, end, playerTurn):
            if start == end:
                # print("Base")
                if playerTurn:
                    return [nums[start], 0]
                else:
                    return [0,nums[end]] 
            
            elif playerTurn:
                # print("one")
                ans = predict(nums, start+1, end, not playerTurn)
                ans[0] += nums[start]
                ans1 = predict(nums, start, end-1, not playerTurn)
                ans1[0] += nums[end]
                if ans[0] > ans1[0]:
                    return ans
                return ans1
            else:
                # print("Two")
                ans = predict(nums, start+1, end, not playerTurn)
                ans[1] += nums[start]
                ans1 = predict(nums, start, end-1, not playerTurn)
                ans1[1] += nums[end]
                if ans[1] > ans1[1]:
                    return ans
                return ans1
        
        res = predict(nums, 0, len(nums)-1, True)
        # print(res)
        if res[0] >= res[1]:
            return True
        
        return False