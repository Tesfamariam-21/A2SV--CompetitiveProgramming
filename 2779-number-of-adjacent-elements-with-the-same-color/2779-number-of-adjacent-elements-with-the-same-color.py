class Solution:
    def colorTheArray(self, n: int, queries: List[List[int]]) -> List[int]:
        
        array = [0] * n
        
        count = 0
        answer = []
        
        for index, color in queries:
            if array[index] == 0:
                array[index] = color
            else:
                if index - 1 >= 0:
                    if array[index-1] == array[index]:
                        count -= 1
                if index + 1 < n:
                    if array[index + 1] == array[index]:
                        count -= 1
                array[index] = color
                
            
            if index - 1 >= 0:
                if array[index-1] == array[index]:
                    count += 1
            if index + 1 < n:
                if array[index + 1] == array[index]:
                    count += 1
            
            answer.append(count)
                                
        return answer