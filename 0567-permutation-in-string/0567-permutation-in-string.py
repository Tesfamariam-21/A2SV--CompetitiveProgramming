class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        if len(s1) > len(s2):
            return False

        ptr = len(s1)
        s1_counter = Counter(s1)
        s2_counter = Counter(s2[:len(s1)])

        if s1_counter == s2_counter:
            return True


        for i in range(ptr, len(s2)):
            s2_counter[s2[i]] +=1
            s2_counter[s2[i-ptr]] -=1

            if s1_counter == s2_counter:
                return True

        return False



        # if len(s1) > len(s2):
        #     return False

        # for i in range(len(s1), len(s2)):
        #     if Counter(s2[i - len(s1) :i]) == Counter(s1):
        #         return True
            
        # return False


































        # if len(s1)> len(s2):
        #     return False
        
        # dictS1, dictS2 = [0]*26, [0]*26
        # matches = 0
        # left = 0

        
        # for i in range(len(s1)):
        #     dictS1[ord(s1[i]) -ord('a')]+=1
        #     dictS2[ord(s2[i]) -ord('a')]+=1
            
        # for i in range(26):
        #     matches +=1 if dictS1[i] == dictS2[i] else 0
            
        # for i in range(len(s1),len(s2)):
        #     if matches == 26:
        #         return True
            
        #     index = ord(s2[i]) - ord('a')
        #     dictS2[index] +=1
        #     if dictS1[index] == dictS2[index]:
        #         matches +=1
        #     elif dictS1[index] +1 == dictS2[index]:
        #         matches -= 1
                
        #     index = ord(s2[left]) - ord('a')
        #     dictS2[index] -=1
        #     if dictS1[index] == dictS2[index]:
        #         matches +=1
        #     elif dictS1[index] -1 == dictS2[index]:
        #         matches -= 1
            
        #     left +=1
            
        
        # return matches == 26        
        
                
                
                
                
                
                