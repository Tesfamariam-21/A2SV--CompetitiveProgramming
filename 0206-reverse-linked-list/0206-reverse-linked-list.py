# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head == None:
            return None
        current = head
        nextNode = current.next
        prevNode = None
        
        while nextNode != None:
            current.next = prevNode
            prevNode = current
            current = nextNode
            nextNode = current.next
        
        current.next = prevNode
        
        return current
        
        