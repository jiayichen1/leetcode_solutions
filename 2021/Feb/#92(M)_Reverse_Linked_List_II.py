# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: ListNode, left: int, right: int) -> ListNode:
        if left == right:
            return head
        
        dummy = ListNode(0, head)
        
        cur, prev = head, dummy
        
        for _ in range(left-1):
            cur, prev = cur.next, prev.next
            
# METHOD from leetcode that I don't really understand            
#         for _ in range(right-left):
#             temp = cur.next
#             cur.next = temp.next
#             temp.next = prev.next
#             prev.next = temp
            
#         return dummy.next
        
        leftBorder = prev
        cur, prev = cur.next, prev.next
        
        for _ in range(right-left):
            temp = cur.next
            cur.next = prev
            prev = cur
            cur = temp
            if temp == None:
                break
        
        leftBorder.next.next = cur
        leftBorder.next = prev
        
        return dummy.next
        