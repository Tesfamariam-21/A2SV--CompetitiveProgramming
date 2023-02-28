class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1)> len(s2):
            return False
        
        dictS1, dictS2 = [0]*26, [0]*26
        matches = 0
        left = 0

        
        for i in range(len(s1)):
            dictS1[ord(s1[i]) -ord('a')]+=1
            dictS2[ord(s2[i]) -ord('a')]+=1
            
        for i in range(26):
            matches +=1 if dictS1[i] == dictS2[i] else 0
            
        for i in range(len(s1),len(s2)):
            if matches == 26:
                return True
            
            index = ord(s2[i]) - ord('a')
            dictS2[index] +=1
            if dictS1[index] == dictS2[index]:
                matches +=1
            elif dictS1[index] +1 == dictS2[index]:
                matches -= 1
                
            index = ord(s2[left]) - ord('a')
            dictS2[index] -=1
            if dictS1[index] == dictS2[index]:
                matches +=1
            elif dictS1[index] -1 == dictS2[index]:
                matches -= 1
            
            left +=1
            
        
        return matches == 26        
        
                
                
                
                
                
                
