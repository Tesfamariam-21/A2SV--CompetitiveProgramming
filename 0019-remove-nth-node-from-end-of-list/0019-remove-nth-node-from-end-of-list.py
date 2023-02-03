# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        fast = head
        slow = head
        count = 0
        size = 0
        
        
        while fast:
            fast = fast.next
            size +=1
            
            if count > n:
                slow = slow.next
            count +=1
            
            if count == 1 and fast == None:
                return None
            elif n == size and fast == None:
                head = head.next
                
        slow.next = slow.next.next
        
        return head