class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        def reverse(left, right):
            if left >= right:
                return
            s[left], s[right] = s[right], s[left]
            
            return reverse(left+1, right-1)
        left = 0
        right = len(s)-1
       
        reverse(left, right)

        
#         left = 0
#         right = len(s) - 1
        
#         while left < right:
#             s[left], s[right] = s[right], s[left]
#             left += 1
#             right -=1
            
            
#         return  s
        