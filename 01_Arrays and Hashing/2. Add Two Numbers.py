# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:

        dummy=ListNode(0)
        current=dummy

        carry=0

        while l1 or l2 or carry:
            if l1:
                val1=l1.val 
            else:
                val1=0
            
            if l2:
                val2=l2.val
            else:
                val2=0
            ans=val1+val2+carry
            if ans >9: 
                carry=1
                ans=ans%10
            else:
                carry=0
            current.next=ListNode(ans)

            current=current.next

            if l1:
                l1=l1.next
            else:
                None
            if l2:
                l2=l2.next
            else:
                None
        return dummy.next
