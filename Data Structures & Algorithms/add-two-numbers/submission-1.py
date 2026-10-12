# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        ptr = prev = ListNode()
        carry = 0
        while l1 and l2:
            sm = l1.val + l2.val + carry
            print(f"sm: {sm % 10}")
            print(f"carry: {sm // 10}")
            temp = ListNode(sm % 10)
            carry = sm // 10
            l1 = l1.next
            l2 = l2.next
            prev.next = temp
            prev = temp

        while l1:
            sm = l1.val + carry
            temp = ListNode((sm % 10))
            carry = sm // 10
            l1 = l1.next
            prev.next = temp
            prev = temp

        while l2:
            sm = l2.val + carry
            temp = ListNode((sm % 10))
            carry = sm // 10
            l2 = l2.next
            prev.next = temp
            prev = temp

        prev.next = ListNode(carry) if carry else None
        
        return ptr.next