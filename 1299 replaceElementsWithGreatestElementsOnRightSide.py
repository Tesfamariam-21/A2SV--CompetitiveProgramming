class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        if(len(arr) == 1):
            return [-1]
        answer = []
        greatest = max(arr[1:])
        greatestIndex = arr.index(greatest)
        for i in range(len(arr)-1):
            if(i == greatestIndex):
                greatest = max(arr[i+1:])
                greatestIndex = arr.index(greatest, i+1)
                answer.append(greatest)
            else:
                answer.append(greatest)
            
        answer.append(-1)
        return answer
