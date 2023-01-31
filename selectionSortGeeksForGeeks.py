class Solution: 
    def select(self, arr, i):
        # code here 
        pass
    
    def selectionSort(self, arr,n):
        #code here
        
        for i in range(len(arr)-1):
            minI = i
            
            for j in range(i+1, len(arr)):
                if arr[minI] > arr[j]:
                    minI = j
            
            if minI != i:
                arr[minI], arr[i] = arr[i], arr[minI]
    
