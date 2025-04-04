class Node(object):
    def __init__(self, data):
        self.data = data
        self.next = None

def remove_duplicates(head):
    # Your code goes here.
    # Remember to return the head of the list.
    if head is None:
        return None
    seen_values = set()
    seen_values.add(head.data)
    current = head
    while current.next:
        if current.next.data in seen_values:
            current.next = current.next.next
        else:
            seen_values.add(current.next.data)
            current = current.next
    return head