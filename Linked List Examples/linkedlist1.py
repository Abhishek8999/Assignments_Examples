"""
Input : head[3, 2, 0, -4], pos = 1
O/P : True
"""

# Check linked list is cyclic or not
class Node(object):
    def __init__(self, value, next=None):
        self.next = next
        self.value = value

# function to create a list
def create_list():
    pos = Node(2)
    head = Node(3, pos)
    head = Node(2, head)
    head = Node(0, head)
    head = Node(-4, head)

    pos.next = head
    return head

# check the list is cicrular or not
def is_circular(head):
    slow = head
    fast = head

    while True:
        slow = slow.next
        fast = fast.next.next

        print(slow.value, fast.value)
        if slow.value == fast.value:
            return True
        elif slow is fast:
            return False

if __name__ == "__main__":
    node = create_list()
    print(is_circular(node))
