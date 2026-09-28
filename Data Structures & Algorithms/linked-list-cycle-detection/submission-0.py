# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        curr = head
        mp = {}
        while curr:
            if curr in mp:
                return True
            mp[curr] = True
            curr = curr.next
        return False
