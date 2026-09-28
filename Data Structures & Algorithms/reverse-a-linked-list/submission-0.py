# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        res = []
        curr = head
        if not head:
            return None
        while curr:
            res.append(curr.val)
            curr = curr.next
        
        res.reverse()
        dummy = ListNode(0)
        curr = dummy
        for val in res:
            curr.next = ListNode(val)
            curr = curr.next
        return dummy.next