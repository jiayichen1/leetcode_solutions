# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        dummyHead = ListNode(0)
        p, q = l1, l2
        carry = 0
        curr = dummyHead
        
        while p != None or q != None:
            if p != None:
                x = p.val
            else:
                x = 0
            if q != None:
                y = q.val
            else:
                y = 0
            sum = x + y + carry
            carry = sum // 10
            curr.next = ListNode(sum%10)
            curr = curr.next
            if p!=None:
                p = p.next
            if q!=None:
                q = q.next
        
        if carry != 0:
            curr.next = ListNode(carry)
            
        return dummyHead.next