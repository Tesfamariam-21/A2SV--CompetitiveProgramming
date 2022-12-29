class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        size = len(arr)
        i=0
        while(i < size):
            if(arr[i] == 0):
                arr.insert(i, 0)
                i +=2
            else: 
                i +=1
                
        for i in range(len(arr) - size):
            arr.pop()
            

               