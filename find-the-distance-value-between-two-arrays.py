class Solution:
    def findTheDistanceValue(self, arr1: List[int], arr2: List[int], d: int) -> int:
        count = 0
        arr2 = sorted(arr2)
        print(arr1, arr2)

        for num in arr1:
            low = 0
            high = len(arr2) - 1
            count +=1

            while low <= high:
                mid = (low + high)//2

                if abs(arr2[mid] - num)  <= d: 
                    count -=1
                    break
                elif arr2[mid] < num:
                    low = mid + 1
                else:
                    high = mid -1


        return count