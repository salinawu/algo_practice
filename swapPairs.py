# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        headPointer = head
        prev = None
        while head is not None:
            if head.next:
                next = head.next
                if prev is not None:
                    prev.next = next
                else:
                    headPointer = next

                head.next = next.next
                next.next = head
                prev = head
                head = head.next
            else:
                return headPointer
        return headPointer