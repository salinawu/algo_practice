from __future__ import print_function

# Given the head of a Singly LinkedList, write a method to modify the LinkedList such that the nodes
# from the second half of the LinkedList are inserted alternately to the nodes from the first half in reverse order.
# So if the LinkedList has nodes 1 -> 2 -> 3 -> 4 -> 5 -> 6 -> null,
# your method should return 1 -> 6 -> 2 -> 5 -> 3 -> 4 -> null. 

class Node:
  def __init__(self, value, next=None):
    self.value = value
    self.next = next

  def print_list(self):
    temp = self
    while temp is not None:
      print(str(temp.value) + " ", end='')
      temp = temp.next
    print()


def reorder(head):
  print("head: ", head.print_list())
  slow, fast = head, head
  while fast is not None and fast.next is not None:
    slow = slow.next
    fast = fast.next.next

  reversed = reverse(slow)

  head_pointer = head
  while reversed is not None:
    prior_next = head_pointer.next
    reversed_next = reversed.next
    reversed.next = prior_next
    head_pointer.next = reversed

    head_pointer = head_pointer.next.next
    reversed = reversed_next

  if head_pointer is not None:
    head_pointer.next = None
  # return head

def reverse(head):
  prev = None
  while head is not None:
    next = head.next
    head.next = prev
    prev = head
    head = next

  return prev

# None
# 1, 2, 3, 4

# 1, None
# 2, 3, 4

# 2, 1, None
# 3, 4


def main():
  head = Node(2)
  head.next = Node(4)
  head.next.next = Node(6)
  head.next.next.next = Node(8)
  head.next.next.next.next = Node(10)
  head.next.next.next.next.next = Node(12)
  reorder(head)
  head.print_list()


main()
