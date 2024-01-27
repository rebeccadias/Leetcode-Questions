# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


        """
class Solution:
    def mergeTwoLists(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        made a dummynode and gave it a value of -1 
        dummynode=ListNode(-1)
        the dummy node and current are the same and have the same structure initially i.e. 
        val is -1 and next is None
        current=dummynode

        while l1 and l2:
            
            if l1.val>=l2.val:
                current=l1.next
                if l1.next !=None:
                    l1=l1.next
            if l2.val>l1.val:
                current=l2.next
                if l2.next !=None:
                    l2=l2.next 

        return dummynode.next




The issue leading to the Time Limit Exceeded (TLE) in your code is related to how you're handling the merging process of the two lists `l1` and `l2`. The logic inside your `while` loop is not correctly advancing the `current` pointer in all cases, which can lead to an infinite loop. Here are some hints to help you debug and fix the issue:

1. **Advance Current Pointer**: After assigning `current.next` to either `l1` or `l2`, you need to move the `current` pointer forward. This is crucial to progress through the newly merged list.

2. **Compare and Attach Nodes**: Your conditional statements for comparing the values in `l1` and `l2` nodes are causing an issue. Think about what happens when `l1.val` is greater than or equal to `l2.val`, and how you should properly advance the `l1` or `l2` pointer after attaching the node to `current`.

3. **Handling Remaining Nodes**: After the `while` loop, you need to check if there are any remaining nodes in either `l1` or `l2`. If one list is exhausted before the other, you should attach the remaining part of the non-exhausted list to `current.next`.

4. **Infinite Loop Detection**: Consider what happens in your current loop when either `l1` or `l2` becomes `None`. How does your loop terminate, and are you correctly updating the `current` pointer to move along the merged list?

By addressing these points, you should be able to fix the TLE issue and ensure your function correctly merges the two linked lists.
        """
      
