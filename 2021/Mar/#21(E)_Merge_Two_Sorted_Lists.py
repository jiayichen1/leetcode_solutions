# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        # create a dummy to hold the head
        dummy = ListNode(0, None)
        # head is used for building the list
        head = dummy
        
        # if either list terminates, exit loop and do one simple step to finish building
        while l1 and l2:
            val1, val2 = l1.val, l2.val
            
            if val1 <= val2:
                head.next = l1
                head = head.next
                l1 = l1.next
            else:
                head.next = l2
                head = head.next
                l2 = l2.next
        
        # if there's some l1 left, connect it; o/w connect l2
        if l1:
            head.next = l1
        elif l2:
            head.next = l2
        
        return dummy.next
        