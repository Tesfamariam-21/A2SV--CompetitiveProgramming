class Solution:
    def removeComments(self, source: List[str]) -> List[str]:
        blocked = False
        li = []
        rec = ""
        cnt = 2
        c = 0
        index = []
        for i in range(len(source)):
            j = 0
            if not blocked:
                rec = ""
            # for j in range(len(source[i])):
            while j < len(source[i]): 
                if source[i][j] in "*/":
                    if j+1 < len(source[i]) and source[i][j:j+2] == '//' and not blocked:
                        break
                        print("what is up")
                    elif j+1 < len(source[i]) and source[i][j:j+2] == '/*' and not blocked:
                        blocked = True
                        j += 2
                        continue
                    elif j+1 < len(source[i]) and source[i][j:j+2] == '*/' and blocked:
                        blocked = False
                        j += 2
                        continue
                if not blocked:
                    rec +=source[i][j]
                    # rec=""
                j +=1
                # print(rec)
                    
                        
            if rec != "" and not blocked:
                li.append(rec)
                rec = ""
                
        return li
    
                    
                
#                 if c > 0:
#                     c -=1
               
#                 if source[i][j: j+3] == "/*/" and blocked:
#                     pass
#                     # blocked = False      
#                 elif source[i][j: j+3] == "/*/" and not blocked:
#                     blocked = True 
#                     c = 2
#                     cnt = 0
#                 elif source[i][j: j+2] == "*/" and not blocked:
#                     rec +=source[i][j]
#                     cnt +=1
#                 elif source[i][j: j+2] == "*/" and blocked and c == 0:
#                     blocked = False
#                     cnt += 1
#                 elif cnt == 1:
#                     cnt +=1
#                 elif source[i][j: j+2] == "/*" and not blocked:
#                     blocked = True
#                     cnt = 0
#                 elif source[i][j: j+2] == "//" and not blocked:
#                     break                    
#                 elif cnt >= 2 and not blocked :
#                     rec +=source[i][j]  
