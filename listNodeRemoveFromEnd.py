# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        dummy = ListNode()
        dummy.next = head
        fasterPointer = dummy
        slowerPointer = dummy
        final = slowerPointer
        
        for i in range(n + 1):
            fasterPointer = fasterPointer.next
            
        while fasterPointer is not None:
            fasterPointer = fasterPointer.next
            slowerPointer = slowerPointer.next
            
        slowerPointer.next = slowerPointer.next.next
        return final.next