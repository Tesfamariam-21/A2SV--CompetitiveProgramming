# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
#         assigning pointers
        right = head
        left = head
        length = 0
        element = 0 # to iterate to the length -k
        
#         base case
        if head == None:
            return
        if k == 0:
            return head
        
#         iterating to get the last element and size of linked list
        while right.next:
            right = right.next
            length +=1
         
#         iterating to lenght - k
        # print(k%length)
#     another base case
       
        if length == 0:
            return head
        elif length+1 == k:
            return head
        
        k = k % (length +1)
        if k == 0:
            return head
        
        while element < (length - k):
            left = left.next
            element +=1

        temp = left.next
        left.next = None
        right.next = head
        head = temp

        
        return head
            
        