class Solution:
    def pancakeSort(self, arr: List[int]) -> List[int]:
        isSorted = False
        length = len(arr)
        index = 0
        ans = []
        
        while(not isSorted):
            Max = max(arr[:length - index])
            # print(Max)
            indexMax = arr.index(Max)
            # print(indexMax)
            if indexMax == length - index:
                arr[:length-index] = reversed(arr[:length - index])
                ans.append(length - index)
            else:
                arr[:indexMax+1] = reversed(arr[:indexMax+1])
                arr[:length-index] = reversed(arr[:length - index])
                ans.append(indexMax+1)
                ans.append(length-index)
            
            if arr == sorted(arr):
                isSorted = True
            index += 1
                
        return ans