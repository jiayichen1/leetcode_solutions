# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        # if no rotation, return
        if k == 0:
            return head
        
        length = 0
        lengthHelper = head  # used for finding the length
        dummy2 = ListNode(0, head)  # used for rotating later
        
        while lengthHelper:
            lengthHelper = lengthHelper.next
            length += 1
        
        # return empty list or length 1 list
        if length == 0 or length == 1:
            return head
        
        k = k % length  # take mod length of k, avoid excessive rotation
        steps = length - k  # number of steps to take to find the new head
        
        # if rotation steps == length, then rotation is stationary
        if steps == length:
            return head
        
        newHead = head
        for i in range(steps-1):
            newHead = newHead.next
        temp = newHead.next       
        newHead.next = None
        newHead = temp
        
        oriHead = dummy2.next
        dummy2.next = newHead
        
        connectionHelper = newHead
        while connectionHelper.next:
            connectionHelper = connectionHelper.next
        
        connectionHelper.next = oriHead
        
        return dummy2.next
        