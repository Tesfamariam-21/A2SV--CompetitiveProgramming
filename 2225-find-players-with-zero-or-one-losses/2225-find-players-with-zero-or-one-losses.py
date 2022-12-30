class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        dict_ = {}
        noLoss = []
        lostOne = []
        ans = []
        for i in range(len(matches)):
            if matches[i][1] in dict_:
                dict_[matches[i][1]] += 1
            else:
                dict_[matches[i][1]] = 1
        

        for i in range(len(matches)):
            for j in range(2):
                k = matches[i][j] 
                if k not in dict_:
                    noLoss.append(k)
                elif dict_[k] == 1:
                    lostOne.append(k)
        noLoss = list(set(noLoss))
        lostOne = list(set(lostOne))
        
        ans.append(sorted(noLoss))
        ans.append(sorted(lostOne))

        
        return ans
        
        