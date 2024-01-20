# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
""" previous mistake i did was not checking if the fast pointers next ka next was present or not . so i need to avoid this mistake"""
class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:

        if head == None: 
            return False
        
        slow=head
        fast=head.next

        while slow!=None:
            if slow==fast:
                return True
            if slow!=None:
                slow = slow.next
            if fast!=None:
                fast = fast.next
                if fast != None:
                    fast = fast.next
                else:
                    return False

        return False
        
