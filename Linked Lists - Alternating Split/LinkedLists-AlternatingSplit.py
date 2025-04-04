class Node(object):
    def __init__(self, data=None):
        self.data = data
        self.next = None
    
class Context(object):
    def __init__(self, first, second):
        self.first = first
        self.second = second

def alternating_split(head):
    if not head or not head.next:
        raise ValueError()
    
    first_head = head
    second_head = head.next
    first = first_head
    second = second_head
    current = second.next
    toggle = True
    
    while current:
        if toggle:
            first.next = current
            first = current
        else:
            second.next = current
            second = current
        current = current.next
        toggle = not toggle

    first.next = None
    second.next = None
    return Context(first_head, second_head)



        