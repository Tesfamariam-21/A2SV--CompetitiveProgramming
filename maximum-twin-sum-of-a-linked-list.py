# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        res=[]
        while head:
            res.append(head.val)
            head=head.next
        
        i=0
        j=len(res)-1
        max_=0
        while(i<j):
            max_=max(max_,res[i]+res[j])
            i+=1
            j-=1
            
        return max_