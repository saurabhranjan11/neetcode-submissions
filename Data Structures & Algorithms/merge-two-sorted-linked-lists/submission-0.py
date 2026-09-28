# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        res = []
        curr = list1
        while curr:
            res.append(curr.val)
            curr = curr.next

        curr = list2
        while curr:
            res.append(curr.val)
            curr = curr.next
        res.sort()

        dummy = ListNode(0)
        curr = dummy
        for val in res:
            curr.next = ListNode(val)
            curr = curr.next
        return dummy.next