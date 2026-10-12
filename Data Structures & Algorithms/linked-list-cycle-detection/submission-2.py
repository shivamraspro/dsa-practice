# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        p1 = dummy = ListNode()
        p2 = head
        p1.next = head
        while p1 and p2:
            if p1 == p2:
                return True
            
            p1 = p1.next
            p2 = p2.next
            if p2:
                p2 = p2.next

        return False