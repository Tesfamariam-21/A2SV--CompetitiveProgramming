class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        tempList = []
        ans = []
        
        for idx,point in enumerate(points):
            d = point[0] ** 2 + point[1] ** 2
            tempList.append([d,idx])
            
        tempList.sort()
        for i in range(k):
            idx = tempList[i][1]
            
            ans.append(points[idx])
        return ans
            
            
        
            
        