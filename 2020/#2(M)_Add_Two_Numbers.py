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

    # Solution V2
    # minor changes to variable naming
    def addTwoNumbers2(self, l1: ListNode, l2: ListNode) -> ListNode:
        # init a dummyHead for return as always
        dummyHead = ListNode(0)
        curr = dummyHead
        # carries 1 over to the next pos if sum at the prev pos > 9
        carry = 0
        
        while l1 != None or l2 != None:
            x = 0 if l1 == None else l1.val
            y = 0 if l2 == None else l2.val
            tempSum = x + y + carry
            carry = tempSum // 10
            curr.next = ListNode(tempSum % 10)
            curr = curr.next
            l1 = l1 if l1 == None else l1.next
            l2 = l2 if l2 == None else l2.next
        
        if carry:
            curr.next = ListNode(carry)
            
        return dummyHead.next
        