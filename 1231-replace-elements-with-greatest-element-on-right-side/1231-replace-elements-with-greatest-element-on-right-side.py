class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:

        max_ = arr[-1]

        for i in range(len(arr)-2, -1, -1):
            if max_ < arr[i]:   
                arr[i], max_ = max_, arr[i]
                
            else:
                arr[i] = max_

        arr[-1] = -1
        return arr

        