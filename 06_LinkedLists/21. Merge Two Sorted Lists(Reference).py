#------------------------------------------ Version 3 Working Code -------------------------

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummynode=ListNode(-1)
        current=dummynode

        while l1 and l2:
            if l1.val<=l2.val:
                current.next=l1
                l1=l1.next
            else:
                current.next=l2
                l2=l2.next
            current=current.next
        if l1:
                current.next=l1
                current=current.next
        if l2:
                current.next =l2
                current=current.next
             
        return dummynode.next



#------------------------------------------ Version 2-------------------------

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummynode=ListNode(-1)
        current=dummynode

        while l1 and l2:
            if l1.val>=l2.val:
                current=l1
                l1=l1.next
            else:
                current=l2
                l2=l2.next
        if l1:
            while l1:
                current=l1
                l1=l1.next
        if l2:
            while l2:
                current =l2
                l2=l2.next

        return dummynode.next
"""
The issue in your current implementation is in how you're updating the `current` pointer and not correctly linking the nodes to form the merged list. Let's go through the main points to address:

1. **Updating Current Pointer**: Inside your `while` loop, when you assign `current = l1` or `current = l2`, you're just moving the `current` pointer to point to `l1` or `l2`. What you need to do instead is link the `current.next` to either `l1` or `l2`, and then update `current` to be `current.next`. This way, you're actually building the new merged list.

2. **Handling Remaining Nodes**: The logic for handling the remaining nodes in either `l1` or `l2` after one list is exhausted is not correctly implemented. Similar to the main loop, you should be attaching the remaining nodes to `current.next` and then advancing the `current` pointer.

To correct these issues, you need to modify the code to ensure that `current.next` is assigned the next node (either from `l1` or `l2`), and then move `current` to `current.next` to continue building the merged list. After the main `while` loop, attach any remaining nodes from `l1` or `l2` to `current.next`.

Implementing these changes should resolve the problem and allow your function to correctly merge the two lists.
"""
#------------------------------------------ Version 1-------------------------
    
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


    """

The issue leading to the Time Limit Exceeded (TLE) in your code is related to how you're handling the merging process of the two lists `l1` and `l2`. The logic inside your `while` loop is not correctly advancing the `current` pointer in all cases, which can lead to an infinite loop. Here are some hints to help you debug and fix the issue:

1. **Advance Current Pointer**: After assigning `current.next` to either `l1` or `l2`, you need to move the `current` pointer forward. This is crucial to progress through the newly merged list.

2. **Compare and Attach Nodes**: Your conditional statements for comparing the values in `l1` and `l2` nodes are causing an issue. Think about what happens when `l1.val` is greater than or equal to `l2.val`, and how you should properly advance the `l1` or `l2` pointer after attaching the node to `current`.

3. **Handling Remaining Nodes**: After the `while` loop, you need to check if there are any remaining nodes in either `l1` or `l2`. If one list is exhausted before the other, you should attach the remaining part of the non-exhausted list to `current.next`.

4. **Infinite Loop Detection**: Consider what happens in your current loop when either `l1` or `l2` becomes `None`. How does your loop terminate, and are you correctly updating the `current` pointer to move along the merged list?

By addressing these points, you should be able to fix the TLE issue and ensure your function correctly merges the two linked lists.
        """
      
