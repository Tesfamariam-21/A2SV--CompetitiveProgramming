class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        if len(arr) == 1:
            return 1
            
        right  = 0
        max_ = 0
        
        
        for i in range(len(arr)):
            if i >=2 and ((arr[i-2] > arr[i-1] < arr[i]) or arr[i-2] < arr[i-1] > arr[i]):
                right +=1
            elif i >=1 and arr[i-1] != arr[i]:
                right =2
            else:
                right =1
            
            max_ = max(max_, right)
        
        
        return max_