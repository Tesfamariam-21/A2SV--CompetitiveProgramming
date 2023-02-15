# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nextLargerNodes(self, head: Optional[ListNode]) -> List[int]:
        if not head.next:
            return [0]
        
        stack = []
        ans = []
        index = 0
 
        while head:
            ans.append(0)            
#             poping and writing on ans 
#             stack contains a tuple of index, val
            while stack and stack[-1][1] < head.val:
                curindex, val = stack.pop()
                ans[curindex] = head.val
            
            stack.append((index, head.val))
            index +=1
            head = head.next
        

        
        return ans
                
                
            