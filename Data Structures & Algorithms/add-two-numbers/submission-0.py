# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy1 = []
        dummy2 = []
        while l1:
            dummy1.insert(0,l1.val)
            l1 = l1.next
        while l2:
            dummy2.insert(0,l2.val)
            l2 = l2.next
        a = int("".join(map(str,(dummy1))))
        b = int("".join(map(str,(dummy2))))
        c = a + b

        dummy = ListNode(0)
        curr = dummy
        for val in str(c)[::-1]:
            curr.next = ListNode(int(val))
            curr = curr.next
        return dummy.next