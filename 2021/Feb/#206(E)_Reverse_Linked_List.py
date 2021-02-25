# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
#     # Recursive solution
#     def reverseList(self, head: ListNode) -> ListNode:
#         if head == None or head.next == None:
#             return head
        
#         newHead = self.reverseList(head.next)
#         head.next.next = head
#         head.next = None
        
#         return newHead
    
    # Iterative solution
    def reverseList(self, head: ListNode) -> ListNode:
        if head == None or head.next == None:
            return head
        
        prev, curr, temp = head, head.next, None
        
        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        
        head.next = None
        
        return prev
    