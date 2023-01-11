class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        ans = []
        
        for i in range(len(boxes)):
            total = 0
            
            for j in range(i, -1, -1):
                if boxes[j] == "1":
                    total+= i-j
            
            for j in range(i+1, len(boxes)):
                if boxes[j] == "1":
                    total += j - i                                       

                    
            ans.append(total)
                
        return ans