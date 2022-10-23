# Check linked list is cyclic or not


class Node(object):
    def __init__(self, value, next=None):
        self.next = next
        self.value = value



# function to create a list
def create_list():
    pos = Node(-1)
    head = Node(1, pos)
    #head = Node(-1, head)
    #head = Node(0, head)
    #head = Node(-4, head)

    pos.next = head
    return head

# check the list is cicrular or not
def is_circular(head):
    slow = fast = head


    while slow and fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            return True
        else:
            print("No cycle is linked list...")
            return False

    return False

if __name__ == "__main__":
    node = create_list()
    print(is_circular(node))
