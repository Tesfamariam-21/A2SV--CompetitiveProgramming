from collections import OrderedDict
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        ans = []
        # left = 0
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
            
#             if s[i] in window_dict:
#                 arr = window_dict.get(s[i])
#                 arr[0] +=1
#                 arr[1] = i
#                 window_dict[s[i]] = arr
#                 index_dict[s[i]] = i
#             else:
#                 window_dict[s[i]] = 1
#                 index_dict[s[i]] = i
            
#             if (right - left)%len(p) == 0:
#                 for i in range(left,right):
#                     if window_dict == dict_:
#                         ans.append(index_dict[s])
                        
 
#         for i in range(len(s)):
#             if s[i] in window_dict:
#                 arr = window_dict.get(s[i])
#                 arr[0] +=1
#                 arr[1] = i
#                 window_dict[s[i]] = arr
#             else:
#                 window_dict[s[i]] = [1,i]
            
#             if i % len(s) == 0:
#                 if dict_ == window_dict:
#                     ans.append()
#                 else:
#                     window_dict = {}
            
            
        
        
        