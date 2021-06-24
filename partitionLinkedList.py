# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: ListNode, x: int) -> ListNode:
        fast = ListNode(0)
        slow = ListNode(0)
        fast_head = fast
        slow_head = slow
        
        while head:
            if head.val < x:
                slow.next = head
                slow = slow.next
            else:
                fast.next = head
                fast = fast.next
            head = head.next
                
        fast.next = None
        slow.next = fast_head.next
            
        return slow_head.next