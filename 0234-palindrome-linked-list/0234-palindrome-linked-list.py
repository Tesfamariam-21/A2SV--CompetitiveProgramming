# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
#         o(1) space
        fast = head
        slow = head
        middleIndex = 0
        
        # // find middle
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
            middleIndex +=1

#         reverse
        prevNode = None
        while slow:
            nextNode = slow.next
            slow.next = prevNode
            prevNode = slow
            slow = nextNode
            
#             check
        left, right = head, prevNode
        
        while right:
            if left.val != right.val:
                return False
            left = left.next
            right = right.next
            
        return True
        
        
            #     this solution works with space
#         nums = []
#         while head:
#             nums.append(head.val)
#             head = head.next
            
#         left = 0 
#         right = len(nums) - 1
        
#         while left <= right:
#             if nums[left] != nums[right]:
#                 return False
#             left +=1
#             right -=1
        
#         return True
