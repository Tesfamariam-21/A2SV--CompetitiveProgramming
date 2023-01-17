class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        
        for k in range(1, len(heights)):
            j = k - 1
            i = k
            
            while j > -1 and heights[i] > heights[j]:
                heights[i], heights[j] = heights[j], heights[i]
                names[i], names[j] = names[j], names[i]
                j -= 1
                i -= 1 
                
            
                    
                    
                    
           
                
#         for i in range(len(heights)):
#             min_index = i
#             for j in range(i,len(heights)):
#                 if heights[min_index] < heights[j]:
#                     min_index = j
                    
#             heights[min_index], heights[i] = heights[i], heights[min_index]
#             names[min_index], names[i] = names[i], names[min_index]
        
#         for i in range(len(heights)):
#             flag = False
#             for j in range(len(heights)-i-1):
#                 if heights[j] < heights[j+1]:
#                     heights[j], heights[j+1] = heights[j+1], heights[j]
#                     names[j], names[j+1] = names[j+1], names[j]
#                     flag= True
                    
#             if flag == False:
#                     break
                    
        return names