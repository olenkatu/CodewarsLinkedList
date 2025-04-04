from preloaded import Node

def swap_pairs(head):
    if head is None or head.next is None:
        return head

    bla = Node(0)
    bla.next = head

    prev = bla
    current = head

    while current and current.next:
        first = current
        second = current.next

        prev.next = second
        first.next = second.next
        second.next = first

        prev = first
        current = first.next

    return bla.next