# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        prevPointer = dummy
        cur = head
        # dummy.next = head
        if not head or head.next == None:
            return head
        
        while cur:
            if cur.next != None and cur.val == cur.next.val:
                while cur.next != None and cur.val == cur.next.val:
                    cur = cur.next
                prevPointer.next = cur.next
            else:
                prevPointer = cur
            cur = cur.next       
            
        return dummy.next