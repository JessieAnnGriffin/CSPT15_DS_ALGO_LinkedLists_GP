"""
Given a reference to the head node of a singly-linked list, write a function
that reverses the linked list in place. The function should return the new head
of the reversed list.
In order to do this in O(1) space (in-place), you cannot make a new list, you
need to use the existing nodes.
In order to do this in O(n) time, you should only have to traverse the list
once.
*Note: If you get stuck, try drawing a picture of a small linked list and
running your function by hand. Does it actually work? Also, don't forget to
consider edge cases (like a list with only 1 or 0 elements).*
"""
class LinkedListNode():
    def __init__(self, value):
        self.value = value
        self.next  = None

# Tom's approach
 def reverse(head_of_list):
     # create a reference to the head_of_list (our current node)
     current_node = head_of_list
     # set a prev and a next to None
     # create a pointer for the prev ()
     prev = None
     # create a pointer for a next
     next = None

     # while the current node exists (traverse the linked list)
     while current_node:
        # set my next pointer to the current node's 'next'
        next = current_node.next
        # my current's next gets set to the prev
        current_node.next = prev
        # set my prev pointer to my current node
        prev = current_node
        # set reference of current to next (increment)
        current_node = next

     # return the node that the prev pointer is currently point to
     return prev

# Allison posted
# def reverse(head):
#     # Your code here
#     next = head.next
#     head.next = None
#     while next:
#         temp = next.next
#         next.next = head
#         head = next
#         next = temp
#     return head

