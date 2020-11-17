"""
Given only a reference to a specific node in a linked list, delete that node from a singly-linked list.
Example:
The code below should first construct a linked list (x -> y -> z) and then delete `y` from the linked list by calling the function `delete_node`. It is your job to write the `delete_node` function.
```python
class LinkedListNode():
    def __init__(self, value):
        self.value = value
        self.next  = None
x = LinkedListNode('X')
y = LinkedListNode('Y')
z = LinkedListNode('Z')
x.next = y
y.next = z
delete_node(y)
```
*Note: We can do this in O(1) time and space! But be aware that our solution will have some side effects...*
"""
class LinkedListNode():
    def __init__(self, value):
        self.value = value
        self.next  = None

def delete_node(delete_this_node):
    # Need to use traversal
    # set my next to the node I want to delete
    next = delete_this_node.next
    # does this node exist
    if next:
        # set this node's value to the value of the next node
        delete_this_node.value = next.value
        # set this node's next to its next
        delete_this_node.next = next.next # sets the next to none
    else:
        raise Exception("This technique does not work for the last node in the list")


x = LinkedListNode('X')
y = LinkedListNode('Y')
z = LinkedListNode('Z')

# move x's data to where y is and then y is out of scope
# current node's next is the item to delete
x.next = y
# so set the current node's next to the node after the next node (the next node of the next node)
# side effect is that you cannot delete the last node
y.next = z

delete_node(y)