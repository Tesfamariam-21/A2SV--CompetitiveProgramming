class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        index1, index2, n = 0, len(arr) - 1, len(arr) - 1

        while index1 < n and arr[index1] < arr[index1 + 1]:
            index1 +=1
        
        while index2 > 0 and arr[index2 - 1] > arr[index2]:
            index2 -=1

        return 0 < index1 == index2 < n 



        # if len(arr) < 3: return False

        # max_ = max(arr)
        # index = arr.index(max_)

        # if index == 0 or index == len(arr):
        #     return False

        # for i in range(index):
        #     if arr[i] >= arr[i + 1]:
        #         return False

        # for i in range(index,len(arr) - 1):
        #     if arr[i] <= arr[i + 1]:
        #         return False

        # return True
