class Solution:
    def prevPermOpt1(self, arr: List[int]) -> List[int]:
        index = maxx = index2= f = 0
        for i in range(len(arr)-1, 0, -1):
            if arr[i] < arr[i-1]:
                index = i -1
                f = 1
                break

        if f:
            for i in range(index+1, len(arr)):
                if maxx < arr[i] <arr[index]:
                    index2 = i
                    maxx = arr[i]
     
        arr[index], arr[index2] = arr[index2], arr[index]

            
        return arr