from collections import OrderedDict
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        ans = []
        right = len(p)
      
        dict_ = Counter(p)
        window_dict = Counter(s[:len(p)])
        
        
        if window_dict == dict_:
            ans.append(right-len(p))
       
        count = 0
        while right < len(s):
            if window_dict == dict_ and right > len(p):
                ans.append(right-len(p))
                print(window_dict[s[right-len(p)]])
                    
            window_dict[s[right - len(p)]] -=1
            if window_dict[s[right- len(p)]] == 0:
                del window_dict[s[right-len(p)]]
   
            window_dict[s[right]] +=1
            right +=1
            count +=1
  
        if window_dict == dict_ and count != 0:
                ans.append(right-len(p))
            
        return ans
