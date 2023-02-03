# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        nums = []
        while head:
            nums.append(head.val)
            head = head.next
            
        left = 0 
        right = len(nums) - 1
        
        while left <= right:
            if nums[left] != nums[right]:
                return False
            left +=1
            right -=1
        
        return True
        
#         fast = head
#         fastIndex = 0
#         slow = head
#         slowIndex = 0
#         checkNode = head
#         prevNode = None
        
#         while fast != None and fast.next != None:
#             prevNode = slow
#             slow = slow.next
#             fast = fast.next.next
#             fastIndex += 2
#             slowIndex += 1
            
          
#         current = slow.next
#         nextNode = slow.next.next
#         prevNode = slow
#         for i in range(slowIndex - fastIndex + 1):
#             current.next = prevNode
#             prevNode = current
#             current = nextNode
#             nextNode = current.next
            
#         current.next = prevNode
        
#         while slow != None and slow.next != None:
            
#             if checkNode == slow.next:
#                 return False
            
#             checkNode =checkNode.next
#             slow = slow.next
            
            
#         return True
        
        
        
        
        
        
            
        