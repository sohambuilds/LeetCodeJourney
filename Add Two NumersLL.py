class ListNode:
     def __init__(self, val=0, next=None):
         self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:

        added = ListNode(val = (l1.val+l2.val)%10)
        carry = (l1.val+l2.val)//10
        cnode=added

        while (l1.next or l2.next):

            if l1.next is not None:
                l1=l1.next
            else:
                l1.val = 0
            if l2.next is not None:
                l2=l2.next
            else:
                l2.val=0       

            cnode.next = ListNode(val = (carry+l1.val+l2.val)%10)
            carry = (carry + l1.val + l2.val)//10
            cnode = cnode.next

        if carry>0:
            cnode.next=ListNode(val = 1)

        return added
